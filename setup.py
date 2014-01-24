import py2exe
from distutils.core import setup

BoGo = dict(
    modules = ["bogo_server"],
    other_resources = [("TYPELIB", 1, file(r"interfaces\\bogo.tlb", "rb").read())],
    dest_base = r"testComServer"
    )

setup(name="BoGo",
      ctypes_com_server = [BoGo],
      zipfile=None,
      )