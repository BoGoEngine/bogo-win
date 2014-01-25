import sys
import comtypes
from comtypes import GUID
import ctypes
import os

import logging
logging.basicConfig(filename=r'D:\bogo.log',level=logging.DEBUG)


# The generated files are in $PYTHON\Lib\site-packages\comtypes\gen\
from comtypes.gen.BoGo import BoGo
from comtypes.gen.TSF import ITfInputProcessorProfiles, \
                             ITfCategoryMgr, \
                             ITfKeystrokeMgr, \
                             ITfInsertAtSelection

# I had to hack through Windoze's registry to find these numbers...
CLSID_TF_InputProcessorProfiles = GUID("{33C53A50-F456-4884-B049-85FD643ECFED}")
CLSID_TF_CategoryMgr            = GUID("{A4B544A1-438D-4B41-9325-869523E2D6C7}")
GUID_TFCAT_TIP_KEYBOARD         = GUID("{34745C63-B2F0-4784-8B67-5E12C8701A31}")

serverGUIDPointer = ctypes.pointer(GUID("{4581A23E-03EA-4614-975B-FF6206A8B840}"))


def text_to_ushort_array(text):
    return ctypes.cast(ctypes.c_wchar_p(text), ctypes.POINTER(ctypes.c_ushort))


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

        description = text_to_ushort_array("BoGo")

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

        # edit_session = EditSession()
        self.input_context = input_context

        if chr(virtual_key_code) == "A":
            # This call is synchronous and won't return after edit_session.DoEditSession() returns
            # after being called by TSF.

            self.commit_text("BoGo")

            # if ret == TS_E_READONLY:
            #     pass

            # FIXME Do something with ret

            out_eaten[0] = True
        else:
            out_eaten[0] = False

    def commit_text(self, text):
        TF_ES_ASYNCDONTCARE   = 0x0
        TF_ES_SYNC            = 0x1
        TF_ES_READ            = 0x2
        TF_ES_READWRITE       = 0x6
        TF_ES_ASYNC           = 0x8

        self.text_to_commit = text_to_ushort_array(text), len(text)
        return self.input_context.RequestEditSession(self.client_id, self, TF_ES_SYNC | TF_ES_READWRITE)

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
        # start_range = self.input_context.GetStart(edit_cookie)
        # start_range.SetText(edit_cookie, 0, )

        text, length = self.text_to_commit

        inserter = self.input_context.QueryInterface(ITfInsertAtSelection)
        out = inserter.InsertTextAtSelection(edit_cookie, 0, text, length)
