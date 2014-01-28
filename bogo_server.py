from __future__ import unicode_literals
import sys
import comtypes
from comtypes import GUID
import ctypes
import os
from itertools import takewhile

import logging
logging.basicConfig(filename=r'D:\bogo.log', level=logging.DEBUG)

# We aren't interested in DEBUG messages from comtypes
comtypes_logger = logging.getLogger("comtypes")
comtypes_logger.setLevel(logging.WARNING)

import bogo
import utils


# The generated files are in $PYTHON\Lib\site-packages\comtypes\gen\
from comtypes.gen.BoGo import BoGo
from comtypes.gen.TSF import *


# I had to hack through Windoze's registry to find these numbers...
CLSID_TF_InputProcessorProfiles = GUID("{33C53A50-F456-4884-B049-85FD643ECFED}")
CLSID_TF_CategoryMgr            = GUID("{A4B544A1-438D-4B41-9325-869523E2D6C7}")
GUID_TFCAT_TIP_KEYBOARD         = GUID("{34745C63-B2F0-4784-8B67-5E12C8701A31}")

TF_ES_ASYNCDONTCARE   = 0x0
TF_ES_SYNC            = 0x1
TF_ES_READ            = 0x2
TF_ES_READWRITE       = 0x6
TF_ES_ASYNC           = 0x8

WM_KEYDOWN = 0x0100
WM_KEYUP   = 0x0101
WM_CHAR    = 0x0102

VK_BACK    = 0x08
VK_CONTROL = 0x11
VK_MENU    = 0x12
VK_SPACE   = 0x20

serverGUIDPointer = ctypes.pointer(GUID("{4581A23E-03EA-4614-975B-FF6206A8B840}"))


class BoGoTextService(BoGo):

    _reg_threading_ = "Apartment"
    _reg_progid_ = "BoGo.Server.1"
    _reg_novers_progid_ = "BoGo.Server"
    _reg_desc_ = "BoGo COM server"
    _reg_clsctx_ = comtypes.CLSCTX_INPROC_SERVER
    # _reg_typelib_ = "interfaces\\bogo.tlb"

    # The _register and _unregister class methods are called by comtypes.server.register
    # as custom hooks for registration and unregistration.

    @classmethod
    def _register(self, registrar):
        registrar._unregister(BoGoTextService, force=True)
        registrar._register(BoGoTextService)

        # Register input profile (supported languages, description,...)
        inputProcessorProfiles = comtypes.client.CreateObject(CLSID_TF_InputProcessorProfiles,
                                    clsctx=comtypes.CLSCTX_INPROC_SERVER,
                                    interface=ITfInputProcessorProfiles)

        profileGUIDPointer = serverGUIDPointer

        description = utils.text_to_ushort_array("BoGo")

        # http://msdn.microsoft.com/en-us/library/windows/desktop/dd318693%28v=vs.85%29.aspx
        VI_VN = 0x042A

        inputProcessorProfiles.Register(serverGUIDPointer)

        inputProcessorProfiles.AddLanguageProfile(
            serverGUIDPointer,
            VI_VN,
            profileGUIDPointer,
            description,
            4,                   # The description is 4-char long
            None,                # We don't have icons
            -1,
            -1)

        # Register categories (whether we do keyboard, voice,...)
        categoryManager = comtypes.client.CreateObject(CLSID_TF_CategoryMgr,
            clsctx=comtypes.CLSCTX_INPROC_SERVER,
            interface=ITfCategoryMgr)

        categoryManager.RegisterCategory(serverGUIDPointer,
            ctypes.pointer(GUID_TFCAT_TIP_KEYBOARD),
            serverGUIDPointer)

    @classmethod
    def _unregister(self, registrar):
        inputProcessorProfiles = comtypes.client.CreateObject(CLSID_TF_InputProcessorProfiles,
                                    clsctx=comtypes.CLSCTX_INPROC_SERVER,
                                    interface=ITfInputProcessorProfiles)

        hr = inputProcessorProfiles.Unregister(serverGUIDPointer)

        registrar._unregister(BoGoTextService)

    #
    # ITfTextInputProcessor
    #

    def Activate(self, thread_manager, client_id):
        logging.debug("Activated")

        self.client_id = client_id
        self.thread_manager = thread_manager

        keystroke_manager = thread_manager.QueryInterface(ITfKeystrokeMgr)
        keystroke_manager.AdviseKeyEventSink(client_id, self, True)

        self.reset()

    def Deactivate(self):
        logging.debug("Deactivated")

        keystroke_manager = self.thread_manager.QueryInterface(ITfKeystrokeMgr)
        keystroke_manager.UnadviseKeyEventSink(self.client_id)

        self.reset()

    #
    # ITfKeyEventSink
    #

    # The OnTestKey* methods are used by TSF to probe whether we will eat/handle the key
    # or not. After an OnTestKey* method returns True (eaten), another OnKey* event will
    # be fired. We will always return True in OnKey* and do all handling in OnTestKey*

    def OnTestKeyDown(self, this, input_context, virtual_key_code, key_info, out_eaten):
        logging.debug("OnTestKeyDown: %s", virtual_key_code)
        # out_eaten[0] = self.we_will_eat(virtual_key_code)

        self.input_context = input_context

        if virtual_key_code == VK_SPACE:
            self.reset()
            out_eaten[0] = False
            return

        if virtual_key_code == VK_BACK:
            # Logic copied from ibus-bogo
            if self.old_string != "":
                deleted_char = self.old_string[-1]
                self.old_string = self.old_string[:-1]
                self.raw_string = self.raw_string[:-1]

                if len(self.old_string) == 0:
                    self.reset()
                else:
                    index = self.raw_string.rfind(deleted_char)
                    self.raw_string = self.raw_string[:-2] if index < 0 else \
                        self.raw_string[:index] + \
                        self.raw_string[(index + 1):]
            out_eaten[0] = False
            return

        if self.we_will_eat(virtual_key_code):

            # FIXME: Refactor the ToAscii code to a function/method
            keyboard_state = (ctypes.c_ubyte * 256)()

            if ctypes.windll.user32.GetKeyboardState(keyboard_state) == 0:
                ctypes.memset(keyboard_state, 0, 256)
                error = ctypes.windll.kernel32.GetLastError()
                logging.debug("GetKeyboardState() Error: %x", error)

            scan_code = (key_info >> 16) & 0xFF
            buff  = ctypes.create_string_buffer(2)
            output = ctypes.windll.user32.ToAscii(virtual_key_code, scan_code, keyboard_state, buff, 0)

            logging.debug("ToAscii() - %s - %s", output, buff.value)
            logging.debug("CTRL: %s ALT: %s", keyboard_state[VK_CONTROL], keyboard_state[VK_MENU])

            def is_key_down(key_state):
                return key_state & (1 << 7) != 0

            if is_key_down(keyboard_state[VK_MENU]) or \
                    is_key_down(keyboard_state[VK_CONTROL]):
                self.reset()
                out_eaten[0] = False
                return

            new_string, raw_string = bogo.process_key(self.old_string, buff.value, self.raw_string)

            same_initial_chars = list(takewhile(unicode.__eq__, zip(self.old_string, self.new_string)))
            n_backspace = len(self.old_string) - len(same_initial_chars)

            self.delete_prev_chars(n_backspace)
            self.commit_text(new_string)

            self.old_string = new_string
            self.raw_string = raw_string
            out_eaten[0] = True
        else:
            out_eaten[0] = False

    def OnKeyDown(self, this, input_context, virtual_key_code, key_info, out_eaten):
        logging.debug("OnKeyDown: %s", virtual_key_code)
        out_eaten[0] = True

    def OnTestKeyUp(self, this, input_context, virtual_key_code, key_info, out_eaten):
        logging.debug("OnTestKeyUp: %s", virtual_key_code)
        out_eaten[0] = False

    def OnKeyUp(self, this, input_context, virtual_key_code, key_info, out_eaten):
        logging.debug("OnKeyUp: %s", virtual_key_code)
        out_eaten[0] = True

    def OnPreservedKey(self, input_context, preserved_key_guid):
        # This thing is used to handle custom shortcut combinations
        pass

    def OnSetFocus(self, we_get_focus):
        logging.debug("OnSetFocus(we_get_focus=%s)", we_get_focus)

    #
    # ITfEditSession
    #

    def DoEditSession(self, edit_cookie):

        TS_DEFAULT_SELECTION = -1
        selection, count = self.input_context.GetSelection(edit_cookie, TS_DEFAULT_SELECTION, 1)

        _range = selection.range

        # FIXME:
        # Manual dispatching with state like this makes me cringe.
        # We should have separate CommitEditSession, DeleteEditSession, etc. classes.
        if self.editing_operation == "commit":
            text, length = self.text_to_commit

            inserter = self.input_context.QueryInterface(ITfInsertAtSelection)
            out = inserter.InsertTextAtSelection(edit_cookie, 0, text, length)

            # Move the carret to the end of our newly inserted string
            # _range.Collapse(edit_cookie, TF_ANCHOR_END)

            # style = TF_SELECTIONSTYLE()
            # style.ase = TF_AE_NONE
            # style.fInterimChar = False

            # new_selection = TF_SELECTION()
            # new_selection.style = style
            # new_selection.range = _range

            # self.input_context.SetSelection(edit_cookie, 1, new_selection)

        elif self.editing_operation == "delete-prev-chars":
            moved_chars = _range.ShiftStart(edit_cookie, -self.delete_count, None)
            logging.debug("moved_chars: %s", moved_chars)

            TF_ST_CORRECTION = 1
            _range.SetText(edit_cookie, TF_ST_CORRECTION, utils.text_to_ushort_array(""), 0)

    #
    # BoGo
    #

    def we_will_eat(self, virtual_key_code):
        # A-Z
        return virtual_key_code in range(65, 91)

    def reset(self):
        logging.debug("reset()")
        self.new_string = ""
        self.old_string = ""
        self.raw_string = ""

    def commit_text(self, text):
        logging.debug("commit_text(%s)", text)
        self.text_to_commit = utils.text_to_ushort_array(text), len(text)

        self.editing_operation = "commit"
        return self.input_context.RequestEditSession(self.client_id, self, TF_ES_SYNC | TF_ES_READWRITE)

    def delete_prev_chars(self, count):
        logging.debug("delete_prev_chars(%s)", count)

        # Somehow SendMessageW still sends a backspace if count == 0 so
        # we have to explicitly check it like this.
        if count <= 0:
            return

        if self.is_in_transitory_context():
            hwnd = self.input_context.GetActiveView().GetWnd()
            for i in range(count):
                ctypes.windll.user32.SendMessageW(hwnd, WM_KEYDOWN, VK_BACK, 1)
                ctypes.windll.user32.SendMessageW(hwnd, WM_KEYUP  , VK_BACK, 1)
                ctypes.windll.user32.SendMessageW(hwnd, WM_CHAR   , VK_BACK, 1)
        else:
            self.editing_operation = "delete-prev-chars"
            self.delete_count = count
            self.input_context.RequestEditSession(self.client_id, self, TF_ES_SYNC | TF_ES_READWRITE)

    def is_in_transitory_context(self):
        # http://blogs.msdn.com/b/tsfaware/archive/2007/04/25/transitory-contexts.aspx
        TS_SS_TRANSITORY = 0x4
        status = self.input_context.GetStatus()

        return status.dwStaticFlags & TS_SS_TRANSITORY != 0
