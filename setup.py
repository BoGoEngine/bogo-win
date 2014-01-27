import py2exe
from distutils.core import setup

BoGo = dict(
    modules = ["bogo_server"],
    other_resources = [("TYPELIB", 1, file(r"interfaces\\bogo.tlb", "rb").read())],
    dest_base = r"bogo",
    create_exe = False
    )

setup(name="BoGo",
      version="0.1.0",
      author="Trung Ngo",
      author_email="ndtrung4419@gmail.com",
      ctypes_com_server = [BoGo],
      zipfile=None,
      options={"py2exe": {"bundle_files": 3, "dll_excludes": ["w9xpopen.exe"]}},
      )