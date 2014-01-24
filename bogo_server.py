import sys
import comtypes
from comtypes import GUID
import ctypes
import os


# The generated files are in $PYTHON\Lib\site-packages\comtypes\gen\
from comtypes.gen.BoGo import BoGo
from comtypes.gen.TSF import ITfInputProcessorProfiles, ITfCategoryMgr

# I had to hack through Windoze's registry to find these numbers...
CLSID_TF_InputProcessorProfiles = "{33C53A50-F456-4884-B049-85FD643ECFED}"
CLSID_TF_CategoryMgr = "{A4B544A1-438D-4B41-9325-869523E2D6C7}"
GUID_TFCAT_TIP_KEYBOARD = GUID("{34745C63-B2F0-4784-8B67-5E12C8701A31}")
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

        description = ctypes.c_wchar_p("BoGo")
        description = ctypes.cast(description, ctypes.POINTER(ctypes.c_ushort))

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

    def Activate(self, thread_manager, client_id):
        pass

    def Deactivate(self):
        pass

