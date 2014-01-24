import sys
import comtypes
from comtypes.server import w_getopt
from comtypes.client import GetModule
from comtypes import GUID
import ctypes
import os


comtypes.client.gen_dir = os.path.dirname(__file__) + "interfaces/gen/"

# generate wrapper code for the type library, this needs
# to be done only once (but also each time the IDL file changes)
GetModule("interfaces/bogo.tlb")
GetModule("interfaces/tsf.tlb")

from interfaces.gen.BoGo import BoGo
from interfaces.gen.TSF import ITfInputProcessorProfiles

# I had to hack through Windoze's registry to find this number...
CLSID_TF_InputProcessorProfiles = "{33C53A50-F456-4884-B049-85FD643ECFED}"


class BoGoTextService(BoGo):

    _reg_threading_ = "Both"
    _reg_progid_ = "BoGo.Server.1"
    _reg_novers_progid_ = "BoGo.Server"
    _reg_desc_ = "BoGo COM server"
    _reg_clsctx_ = comtypes.CLSCTX_INPROC_SERVER

    def Activate(self, thread_manager, client_id):
        pass

    def Deactivate(self):
        pass


def register_server_with_TSF():
    inputProcessorProfiles = comtypes.client.CreateObject(CLSID_TF_InputProcessorProfiles,
                                clsctx=comtypes.CLSCTX_INPROC_SERVER,
                                interface=ITfInputProcessorProfiles)

    serverGUIDPointer = ctypes.pointer(GUID("{4581A23E-03EA-4614-975B-FF6206A8B840}"))
    profileGUIDPointer = serverGUIDPointer

    description = ctypes.c_wchar_p("BoGo")
    description = ctypes.cast(description, ctypes.POINTER(ctypes.c_ushort))

    # http://msdn.microsoft.com/en-us/library/windows/desktop/dd318693%28v=vs.85%29.aspx
    VI_VN = 0x012A
    
    inputProcessorProfiles.Register(serverGUIDPointer)

    inputProcessorProfiles.AddLanguageProfile(
        serverGUIDPointer,
        VI_VN,
        profileGUIDPointer,
        description,
        4,
        None,
        -1,
        -1)


if __name__=='__main__':
    # ni only for 1.4!
    from comtypes.server.register import UseCommandLine
    UseCommandLine(BoGoTextService)

    opts, args = w_getopt.w_getopt(sys.argv[1:],
                                   "regserver unregserver embedding l: f: nodebug")

    if opts:
        for option, value in opts:
            if option == "regserver":
                register_server_with_TSF()