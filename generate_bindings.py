from comtypes.client import GetModule

# comtypes.client.gen_dir = os.path.dirname(__file__) + "interfaces/gen/"

# generate wrapper code for the type library, this needs
# to be done only once (but also each time the IDL file changes)
GetModule("interfaces/bogo.tlb")
GetModule("interfaces/tsf.tlb")