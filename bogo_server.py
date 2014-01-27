import sys
import comtypes
from comtypes import GUID
import ctypes
import os

import logging
logging.basicConfig(filename=r'D:\bogo.log',level=logging.DEBUG)

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

        hr = inputProcessorProfiles.Register(serverGUIDPointer)

        print(hr)

        hr = inputProcessorProfiles.AddLanguageProfile(
            serverGUIDPointer,
            VI_VN,
            profileGUIDPointer,
            description,
            4,                   # The description is 4-char long
            None,                # We don't have icons
            -1,
            -1)

        print(hr)

        # Register categories (whether we do keyboard, voice,...)
        categoryManager = comtypes.client.CreateObject(CLSID_TF_CategoryMgr,
            clsctx=comtypes.CLSCTX_INPROC_SERVER,
            interface=ITfCategoryMgr)

        hr = categoryManager.RegisterCategory(serverGUIDPointer,
            ctypes.pointer(GUID_TFCAT_TIP_KEYBOARD),
            serverGUIDPointer)

        print(hr)

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

        keystroke_manager = thread_manager.QueryInterface(ITfKeystrokeMgr)
        keystroke_manager.AdviseKeyEventSink(client_id, self, True)

    def Deactivate(self):
        logging.debug("Deactivated")

    #
    # ITfKeyEventSink
    #

    # The OnTestKey* methods are used by TSF to probe whether we will eat/handle the key
    # or not. After an OnTestKey* method returns True (eaten), another OnKey* event will
    # be fired.

    def OnTestKeyDown(self, this, input_context, virtual_key_code, key_info, out_eaten):
        logging.debug("OnTestKeyDown: %s", virtual_key_code)

        self.input_context = input_context

        if chr(virtual_key_code) == "A":
            self.delete_prev_chars(4)

            out_eaten[0] = True
        elif chr(virtual_key_code) == "B":
            self.commit_text("BoGo")
            out_eaten[0] = True
        else:
            out_eaten[0] = False

    def commit_text(self, text):
        self.text_to_commit = utils.text_to_ushort_array(text), len(text)

        self.editing_operation = "commit"
        return self.input_context.RequestEditSession(self.client_id, self, TF_ES_SYNC | TF_ES_READWRITE)

    def delete_prev_chars(self, count):

        TS_SS_TRANSITORY = 0x4
        status = self.input_context.GetStatus()

        # http://blogs.msdn.com/b/tsfaware/archive/2007/04/25/transitory-contexts.aspx
        is_in_transitory_context = status.dwStaticFlags & TS_SS_TRANSITORY != 0
        logging.debug("Is in transitory state: %s", is_in_transitory_context)

        if is_in_transitory_context:
            shell = comtypes.client.CreateObject("WScript.Shell")
            for i in xrange(count):
                shell.SendKeys("{Backspace}")
        else:
            self.editing_operation = "delete-prev-chars"
            self.delete_count = count
            self.input_context.RequestEditSession(self.client_id, self, TF_ES_SYNC | TF_ES_READWRITE)

    def OnKeyDown(self, this, input_context, virtual_key_code, key_info, out_eaten):
        logging.debug("OnKeyDown: %s", virtual_key_code)
        out_eaten[0] = True

    def OnTestKeyUp(self, this, input_context, virtual_key_code, key_info, out_eaten):
        logging.debug("OnTestKeyUp: %s", virtual_key_code)
        out_eaten[0] = False

    def OnKeyUp(self, this, input_context, virtual_key_code, key_info, out_eaten):
        logging.debug("OnKeyUp: %s", virtual_key_code)
        out_eaten[0] = False

    def OnPreservedKey(self, input_context, preserved_key_guid):
        pass

    def OnSetFocus(self, we_get_focus):
        logging.debug("OnSetFocus: we_get_focus? %s", we_get_focus)

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
            _range.Collapse(edit_cookie, TF_ANCHOR_END)

            style = TF_SELECTIONSTYLE()
            style.ase = TF_AE_NONE
            style.fInterimChar = False

            new_selection = TF_SELECTION()
            new_selection.style = style
            new_selection.range = _range

            self.input_context.SetSelection(edit_cookie, 1, new_selection)

        elif self.editing_operation == "delete-prev-chars":
            moved_chars = _range.ShiftStart(edit_cookie, -self.delete_count, None)
            logging.debug("moved_chars: %s", moved_chars)

            TF_ST_CORRECTION = 1
            _range.SetText(edit_cookie, TF_ST_CORRECTION, utils.text_to_ushort_array(""), 0)
