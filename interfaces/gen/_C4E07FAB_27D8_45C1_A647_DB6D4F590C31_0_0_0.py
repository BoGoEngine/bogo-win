# -*- coding: mbcs -*-
typelib_path = 'd:\\bogo\\bogo-win32\\interfaces\\bogo.tlb'
_lcid = 0 # change this if required
from ctypes import *
import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0
from comtypes import GUID
from ctypes import HRESULT
from comtypes import helpstring
from comtypes import COMMETHOD
from comtypes import dispid
TfEditCookie = c_ulong
from comtypes import _COAUTHIDENTITY
from comtypes import wireHWND
WSTRING = c_wchar_p
from comtypes import IUnknown
from ctypes.wintypes import _FILETIME
from ctypes.wintypes import _FILETIME
from comtypes.automation import VARIANT
from comtypes import IPersist
from ctypes.wintypes import _ULARGE_INTEGER
from ctypes.wintypes import tagPOINT
from ctypes.wintypes import tagRECT
from ctypes.wintypes import _LARGE_INTEGER
from ctypes.wintypes import _ULARGE_INTEGER
from comtypes import CoClass
TfClientId = c_ulong
from ctypes.wintypes import tagPOINT
from comtypes import BSTR
from ctypes.wintypes import tagRECT
from comtypes import _COSERVERINFO
from comtypes import tagBIND_OPTS2
from comtypes import tagBIND_OPTS2
from comtypes import _COAUTHINFO
from comtypes.automation import VARIANT


class IEnumTfProperties(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{19188CB0-ACA9-11D2-AFC5-00105A2799B5}')
    _idlflags_ = []
    def __iter__(self):
        return self

    def next(self):
        item, fetched = self.Next(1)
        if fetched:
            return item
        raise StopIteration

    def __getitem__(self, index):
        self.Reset()
        self.Skip(index)
        item, fetched = self.Next(1)
        if fetched:
            return item
        raise IndexError(index)

class ITfReadOnlyProperty(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{17D49A3D-F8B8-4B2F-B254-52319DD64C53}')
    _idlflags_ = []
class ITfProperty(ITfReadOnlyProperty):
    _case_insensitive_ = True
    _iid_ = GUID('{E2449660-9542-11D2-BF46-00105A2799B5}')
    _idlflags_ = []
IEnumTfProperties._methods_ = [
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IEnumTfProperties)), 'ppenum' )),
    COMMETHOD([], HRESULT, 'Next',
              ( ['in'], c_ulong, 'ulCount' ),
              ( ['out'], POINTER(POINTER(ITfProperty)), 'ppProp' ),
              ( ['out'], POINTER(c_ulong), 'pcFetched' )),
    COMMETHOD([], HRESULT, 'Reset'),
    COMMETHOD([], HRESULT, 'Skip',
              ( ['in'], c_ulong, 'ulCount' )),
]
################################################################
## code template for IEnumTfProperties implementation
##class IEnumTfProperties_Impl(object):
##    def Reset(self):
##        '-no docstring-'
##        #return 
##
##    def Skip(self, ulCount):
##        '-no docstring-'
##        #return 
##
##    def Clone(self):
##        '-no docstring-'
##        #return ppenum
##
##    def Next(self, ulCount):
##        '-no docstring-'
##        #return ppProp, pcFetched
##

class tagLOGPALETTE(Structure):
    pass
class tagPALETTEENTRY(Structure):
    pass
tagLOGPALETTE._pack_ = 2
tagLOGPALETTE._fields_ = [
    ('palVersion', c_ushort),
    ('palNumEntries', c_ushort),
    ('palPalEntry', POINTER(tagPALETTEENTRY)),
]
assert sizeof(tagLOGPALETTE) == 8, sizeof(tagLOGPALETTE)
assert alignment(tagLOGPALETTE) == 2, alignment(tagLOGPALETTE)
tagPALETTEENTRY._fields_ = [
    ('peRed', c_ubyte),
    ('peGreen', c_ubyte),
    ('peBlue', c_ubyte),
    ('peFlags', c_ubyte),
]
assert sizeof(tagPALETTEENTRY) == 4, sizeof(tagPALETTEENTRY)
assert alignment(tagPALETTEENTRY) == 1, alignment(tagPALETTEENTRY)
class _userFLAG_STGMEDIUM(Structure):
    pass
wireFLAG_STGMEDIUM = POINTER(_userFLAG_STGMEDIUM)
class __MIDL_IWinTypes_0003(Union):
    pass
class _FLAGGED_BYTE_BLOB(Structure):
    pass
__MIDL_IWinTypes_0003._fields_ = [
    ('hInproc', c_int),
    ('hRemote', POINTER(_FLAGGED_BYTE_BLOB)),
    ('hInproc64', c_longlong),
]
assert sizeof(__MIDL_IWinTypes_0003) == 8, sizeof(__MIDL_IWinTypes_0003)
assert alignment(__MIDL_IWinTypes_0003) == 8, alignment(__MIDL_IWinTypes_0003)
class _userHMETAFILE(Structure):
    pass
class __MIDL_IWinTypes_0004(Union):
    pass
class _BYTE_BLOB(Structure):
    pass
__MIDL_IWinTypes_0004._fields_ = [
    ('hInproc', c_int),
    ('hRemote', POINTER(_BYTE_BLOB)),
    ('hInproc64', c_longlong),
]
assert sizeof(__MIDL_IWinTypes_0004) == 8, sizeof(__MIDL_IWinTypes_0004)
assert alignment(__MIDL_IWinTypes_0004) == 8, alignment(__MIDL_IWinTypes_0004)
_userHMETAFILE._fields_ = [
    ('fContext', c_int),
    ('u', __MIDL_IWinTypes_0004),
]
assert sizeof(_userHMETAFILE) == 16, sizeof(_userHMETAFILE)
assert alignment(_userHMETAFILE) == 8, alignment(_userHMETAFILE)
class IDataObject(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{0000010E-0000-0000-C000-000000000046}')
    _idlflags_ = []
class tagFORMATETC(Structure):
    pass
class _userSTGMEDIUM(Structure):
    pass
wireSTGMEDIUM = POINTER(_userSTGMEDIUM)
class IEnumFORMATETC(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{00000103-0000-0000-C000-000000000046}')
    _idlflags_ = []
class IAdviseSink(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{0000010F-0000-0000-C000-000000000046}')
    _idlflags_ = []
class IEnumSTATDATA(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{00000105-0000-0000-C000-000000000046}')
    _idlflags_ = []
IDataObject._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteGetData',
              ( ['in'], POINTER(tagFORMATETC), 'pformatetcIn' ),
              ( ['out'], POINTER(wireSTGMEDIUM), 'pRemoteMedium' )),
    COMMETHOD([], HRESULT, 'RemoteGetDataHere',
              ( ['in'], POINTER(tagFORMATETC), 'pformatetc' ),
              ( ['in', 'out'], POINTER(wireSTGMEDIUM), 'pRemoteMedium' )),
    COMMETHOD([], HRESULT, 'QueryGetData',
              ( ['in'], POINTER(tagFORMATETC), 'pformatetc' )),
    COMMETHOD([], HRESULT, 'GetCanonicalFormatEtc',
              ( ['in'], POINTER(tagFORMATETC), 'pformatectIn' ),
              ( ['out'], POINTER(tagFORMATETC), 'pformatetcOut' )),
    COMMETHOD([], HRESULT, 'RemoteSetData',
              ( ['in'], POINTER(tagFORMATETC), 'pformatetc' ),
              ( ['in'], POINTER(wireFLAG_STGMEDIUM), 'pmedium' ),
              ( ['in'], c_int, 'fRelease' )),
    COMMETHOD([], HRESULT, 'EnumFormatEtc',
              ( ['in'], c_ulong, 'dwDirection' ),
              ( ['out'], POINTER(POINTER(IEnumFORMATETC)), 'ppenumFormatEtc' )),
    COMMETHOD([], HRESULT, 'DAdvise',
              ( ['in'], POINTER(tagFORMATETC), 'pformatetc' ),
              ( ['in'], c_ulong, 'advf' ),
              ( ['in'], POINTER(IAdviseSink), 'pAdvSink' ),
              ( ['out'], POINTER(c_ulong), 'pdwConnection' )),
    COMMETHOD([], HRESULT, 'DUnadvise',
              ( ['in'], c_ulong, 'dwConnection' )),
    COMMETHOD([], HRESULT, 'EnumDAdvise',
              ( ['out'], POINTER(POINTER(IEnumSTATDATA)), 'ppenumAdvise' )),
]
################################################################
## code template for IDataObject implementation
##class IDataObject_Impl(object):
##    def DUnadvise(self, dwConnection):
##        '-no docstring-'
##        #return 
##
##    def GetCanonicalFormatEtc(self, pformatectIn):
##        '-no docstring-'
##        #return pformatetcOut
##
##    def EnumDAdvise(self):
##        '-no docstring-'
##        #return ppenumAdvise
##
##    def DAdvise(self, pformatetc, advf, pAdvSink):
##        '-no docstring-'
##        #return pdwConnection
##
##    def QueryGetData(self, pformatetc):
##        '-no docstring-'
##        #return 
##
##    def EnumFormatEtc(self, dwDirection):
##        '-no docstring-'
##        #return ppenumFormatEtc
##
##    def RemoteSetData(self, pformatetc, pmedium, fRelease):
##        '-no docstring-'
##        #return 
##
##    def RemoteGetData(self, pformatetcIn):
##        '-no docstring-'
##        #return pRemoteMedium
##
##    def RemoteGetDataHere(self, pformatetc):
##        '-no docstring-'
##        #return pRemoteMedium
##

_FLAGGED_BYTE_BLOB._fields_ = [
    ('fFlags', c_ulong),
    ('clSize', c_ulong),
    ('abData', POINTER(c_ubyte)),
]
assert sizeof(_FLAGGED_BYTE_BLOB) == 12, sizeof(_FLAGGED_BYTE_BLOB)
assert alignment(_FLAGGED_BYTE_BLOB) == 4, alignment(_FLAGGED_BYTE_BLOB)
class _STGMEDIUM_UNION(Structure):
    pass
class __MIDL_IAdviseSink_0003(Union):
    pass
class _userHMETAFILEPICT(Structure):
    pass
class _userHENHMETAFILE(Structure):
    pass
class _GDI_OBJECT(Structure):
    pass
class _userHGLOBAL(Structure):
    pass
__MIDL_IAdviseSink_0003._fields_ = [
    ('hMetaFilePict', POINTER(_userHMETAFILEPICT)),
    ('hHEnhMetaFile', POINTER(_userHENHMETAFILE)),
    ('hGdiHandle', POINTER(_GDI_OBJECT)),
    ('hGlobal', POINTER(_userHGLOBAL)),
    ('lpszFileName', WSTRING),
    ('pstm', POINTER(_BYTE_BLOB)),
    ('pstg', POINTER(_BYTE_BLOB)),
]
assert sizeof(__MIDL_IAdviseSink_0003) == 4, sizeof(__MIDL_IAdviseSink_0003)
assert alignment(__MIDL_IAdviseSink_0003) == 4, alignment(__MIDL_IAdviseSink_0003)
_STGMEDIUM_UNION._fields_ = [
    ('tymed', c_ulong),
    ('u', __MIDL_IAdviseSink_0003),
]
assert sizeof(_STGMEDIUM_UNION) == 8, sizeof(_STGMEDIUM_UNION)
assert alignment(_STGMEDIUM_UNION) == 4, alignment(_STGMEDIUM_UNION)
_userSTGMEDIUM._fields_ = [
    ('DUMMYUNIONNAME', _STGMEDIUM_UNION),
    ('pUnkForRelease', POINTER(IUnknown)),
]
assert sizeof(_userSTGMEDIUM) == 12, sizeof(_userSTGMEDIUM)
assert alignment(_userSTGMEDIUM) == 4, alignment(_userSTGMEDIUM)
_userFLAG_STGMEDIUM._fields_ = [
    ('ContextFlags', c_int),
    ('fPassOwnership', c_int),
    ('Stgmed', _userSTGMEDIUM),
]
assert sizeof(_userFLAG_STGMEDIUM) == 20, sizeof(_userFLAG_STGMEDIUM)
assert alignment(_userFLAG_STGMEDIUM) == 4, alignment(_userFLAG_STGMEDIUM)
class _userCLIPFORMAT(Structure):
    pass
wireCLIPFORMAT = POINTER(_userCLIPFORMAT)
class tagDVTARGETDEVICE(Structure):
    pass
tagFORMATETC._fields_ = [
    ('cfFormat', wireCLIPFORMAT),
    ('ptd', POINTER(tagDVTARGETDEVICE)),
    ('dwAspect', c_ulong),
    ('lindex', c_int),
    ('tymed', c_ulong),
]
assert sizeof(tagFORMATETC) == 20, sizeof(tagFORMATETC)
assert alignment(tagFORMATETC) == 4, alignment(tagFORMATETC)
class IRunningObjectTable(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{00000010-0000-0000-C000-000000000046}')
    _idlflags_ = []
class IPersistStream(IPersist):
    _case_insensitive_ = True
    _iid_ = GUID('{00000109-0000-0000-C000-000000000046}')
    _idlflags_ = []
class IMoniker(IPersistStream):
    _case_insensitive_ = True
    _iid_ = GUID('{0000000F-0000-0000-C000-000000000046}')
    _idlflags_ = []
class IEnumMoniker(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{00000102-0000-0000-C000-000000000046}')
    _idlflags_ = []
IRunningObjectTable._methods_ = [
    COMMETHOD([], HRESULT, 'Register',
              ( ['in'], c_ulong, 'grfFlags' ),
              ( ['in'], POINTER(IUnknown), 'punkObject' ),
              ( ['in'], POINTER(IMoniker), 'pmkObjectName' ),
              ( ['out'], POINTER(c_ulong), 'pdwRegister' )),
    COMMETHOD([], HRESULT, 'Revoke',
              ( ['in'], c_ulong, 'dwRegister' )),
    COMMETHOD([], HRESULT, 'IsRunning',
              ( ['in'], POINTER(IMoniker), 'pmkObjectName' )),
    COMMETHOD([], HRESULT, 'GetObject',
              ( ['in'], POINTER(IMoniker), 'pmkObjectName' ),
              ( ['out'], POINTER(POINTER(IUnknown)), 'ppunkObject' )),
    COMMETHOD([], HRESULT, 'NoteChangeTime',
              ( ['in'], c_ulong, 'dwRegister' ),
              ( ['in'], POINTER(_FILETIME), 'pfiletime' )),
    COMMETHOD([], HRESULT, 'GetTimeOfLastChange',
              ( ['in'], POINTER(IMoniker), 'pmkObjectName' ),
              ( ['out'], POINTER(_FILETIME), 'pfiletime' )),
    COMMETHOD([], HRESULT, 'EnumRunning',
              ( ['out'], POINTER(POINTER(IEnumMoniker)), 'ppenumMoniker' )),
]
################################################################
## code template for IRunningObjectTable implementation
##class IRunningObjectTable_Impl(object):
##    def Register(self, grfFlags, punkObject, pmkObjectName):
##        '-no docstring-'
##        #return pdwRegister
##
##    def IsRunning(self, pmkObjectName):
##        '-no docstring-'
##        #return 
##
##    def GetTimeOfLastChange(self, pmkObjectName):
##        '-no docstring-'
##        #return pfiletime
##
##    def GetObject(self, pmkObjectName):
##        '-no docstring-'
##        #return ppunkObject
##
##    def NoteChangeTime(self, dwRegister, pfiletime):
##        '-no docstring-'
##        #return 
##
##    def EnumRunning(self):
##        '-no docstring-'
##        #return ppenumMoniker
##
##    def Revoke(self, dwRegister):
##        '-no docstring-'
##        #return 
##

IEnumFORMATETC._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteNext',
              ( ['in'], c_ulong, 'celt' ),
              ( ['out'], POINTER(tagFORMATETC), 'rgelt' ),
              ( ['out'], POINTER(c_ulong), 'pceltFetched' )),
    COMMETHOD([], HRESULT, 'Skip',
              ( ['in'], c_ulong, 'celt' )),
    COMMETHOD([], HRESULT, 'Reset'),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IEnumFORMATETC)), 'ppenum' )),
]
################################################################
## code template for IEnumFORMATETC implementation
##class IEnumFORMATETC_Impl(object):
##    def Reset(self):
##        '-no docstring-'
##        #return 
##
##    def Skip(self, celt):
##        '-no docstring-'
##        #return 
##
##    def Clone(self):
##        '-no docstring-'
##        #return ppenum
##
##    def RemoteNext(self, celt):
##        '-no docstring-'
##        #return rgelt, pceltFetched
##

class __MIDL_IWinTypes_0001(Union):
    pass
__MIDL_IWinTypes_0001._fields_ = [
    ('dwValue', c_ulong),
    ('pwszName', WSTRING),
]
assert sizeof(__MIDL_IWinTypes_0001) == 4, sizeof(__MIDL_IWinTypes_0001)
assert alignment(__MIDL_IWinTypes_0001) == 4, alignment(__MIDL_IWinTypes_0001)
_userCLIPFORMAT._fields_ = [
    ('fContext', c_int),
    ('u', __MIDL_IWinTypes_0001),
]
assert sizeof(_userCLIPFORMAT) == 8, sizeof(_userCLIPFORMAT)
assert alignment(_userCLIPFORMAT) == 4, alignment(_userCLIPFORMAT)
class TF_SELECTION(Structure):
    _recordinfo_ = ('{C4E07FAB-27D8-45C1-A647-DB6D4F590C31}', 0, 0, 0L, '{75EB22F2-B0BF-46A8-8006-975A3B6EFCF1}')
class ITfRange(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{AA80E7FF-2021-11D2-93E0-0060B067B86E}')
    _idlflags_ = []
class TF_SELECTIONSTYLE(Structure):
    _recordinfo_ = ('{C4E07FAB-27D8-45C1-A647-DB6D4F590C31}', 0, 0, 0L, '{36AE42A4-6989-4BDC-B48A-6137B7BF2E42}')

# values for enumeration '__MIDL_ITfContext_0001'
TF_AE_NONE = 0
TF_AE_START = 1
TF_AE_END = 2
__MIDL_ITfContext_0001 = c_int # enum
TfActiveSelEnd = __MIDL_ITfContext_0001
TF_SELECTIONSTYLE._fields_ = [
    ('ase', TfActiveSelEnd),
    ('fInterimChar', c_int),
]
assert sizeof(TF_SELECTIONSTYLE) == 8, sizeof(TF_SELECTIONSTYLE)
assert alignment(TF_SELECTIONSTYLE) == 4, alignment(TF_SELECTIONSTYLE)
TF_SELECTION._fields_ = [
    ('range', POINTER(ITfRange)),
    ('style', TF_SELECTIONSTYLE),
]
assert sizeof(TF_SELECTION) == 12, sizeof(TF_SELECTION)
assert alignment(TF_SELECTION) == 4, alignment(TF_SELECTION)
class IEnumString(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{00000101-0000-0000-C000-000000000046}')
    _idlflags_ = []
IEnumString._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteNext',
              ( ['in'], c_ulong, 'celt' ),
              ( ['out'], POINTER(WSTRING), 'rgelt' ),
              ( ['out'], POINTER(c_ulong), 'pceltFetched' )),
    COMMETHOD([], HRESULT, 'Skip',
              ( ['in'], c_ulong, 'celt' )),
    COMMETHOD([], HRESULT, 'Reset'),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IEnumString)), 'ppenum' )),
]
################################################################
## code template for IEnumString implementation
##class IEnumString_Impl(object):
##    def Reset(self):
##        '-no docstring-'
##        #return 
##
##    def Skip(self, celt):
##        '-no docstring-'
##        #return 
##
##    def Clone(self):
##        '-no docstring-'
##        #return ppenum
##
##    def RemoteNext(self, celt):
##        '-no docstring-'
##        #return rgelt, pceltFetched
##

class IEnumTfRanges(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{F99D3F40-8E32-11D2-BF46-00105A2799B5}')
    _idlflags_ = []
    def __iter__(self):
        return self

    def next(self):
        item, fetched = self.Next(1)
        if fetched:
            return item
        raise StopIteration

    def __getitem__(self, index):
        self.Reset()
        self.Skip(index)
        item, fetched = self.Next(1)
        if fetched:
            return item
        raise IndexError(index)

class ITfContext(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{AA80E7FD-2021-11D2-93E0-0060B067B86E}')
    _idlflags_ = []
ITfReadOnlyProperty._methods_ = [
    COMMETHOD([], HRESULT, 'GetType',
              ( ['out'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'pguid' )),
    COMMETHOD([], HRESULT, 'EnumRanges',
              ( ['in'], TfEditCookie, 'ec' ),
              ( ['out'], POINTER(POINTER(IEnumTfRanges)), 'ppenum' ),
              ( ['in'], POINTER(ITfRange), 'pTargetRange' )),
    COMMETHOD([], HRESULT, 'GetValue',
              ( ['in'], TfEditCookie, 'ec' ),
              ( ['in'], POINTER(ITfRange), 'pRange' ),
              ( ['out'], POINTER(VARIANT), 'pvarValue' )),
    COMMETHOD([], HRESULT, 'GetContext',
              ( ['out'], POINTER(POINTER(ITfContext)), 'ppContext' )),
]
################################################################
## code template for ITfReadOnlyProperty implementation
##class ITfReadOnlyProperty_Impl(object):
##    def GetValue(self, ec, pRange):
##        '-no docstring-'
##        #return pvarValue
##
##    def GetType(self):
##        '-no docstring-'
##        #return pguid
##
##    def GetContext(self):
##        '-no docstring-'
##        #return ppContext
##
##    def EnumRanges(self, ec, pTargetRange):
##        '-no docstring-'
##        #return ppenum
##


# values for enumeration '__MIDL___MIDL_itf_bogo_0001_0064_0001'
TF_ANCHOR_START = 0
TF_ANCHOR_END = 1
__MIDL___MIDL_itf_bogo_0001_0064_0001 = c_int # enum
TfAnchor = __MIDL___MIDL_itf_bogo_0001_0064_0001
class ITfPropertyStore(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{6834B120-88CB-11D2-BF45-00105A2799B5}')
    _idlflags_ = []
ITfProperty._methods_ = [
    COMMETHOD([], HRESULT, 'FindRange',
              ( ['in'], TfEditCookie, 'ec' ),
              ( ['in'], POINTER(ITfRange), 'pRange' ),
              ( ['out'], POINTER(POINTER(ITfRange)), 'ppRange' ),
              ( ['in'], TfAnchor, 'aPos' )),
    COMMETHOD([], HRESULT, 'SetValueStore',
              ( ['in'], TfEditCookie, 'ec' ),
              ( ['in'], POINTER(ITfRange), 'pRange' ),
              ( ['in'], POINTER(ITfPropertyStore), 'pPropStore' )),
    COMMETHOD([], HRESULT, 'SetValue',
              ( ['in'], TfEditCookie, 'ec' ),
              ( ['in'], POINTER(ITfRange), 'pRange' ),
              ( ['in'], POINTER(VARIANT), 'pvarValue' )),
    COMMETHOD([], HRESULT, 'Clear',
              ( ['in'], TfEditCookie, 'ec' ),
              ( ['in'], POINTER(ITfRange), 'pRange' )),
]
################################################################
## code template for ITfProperty implementation
##class ITfProperty_Impl(object):
##    def FindRange(self, ec, pRange, aPos):
##        '-no docstring-'
##        #return ppRange
##
##    def Clear(self, ec, pRange):
##        '-no docstring-'
##        #return 
##
##    def SetValueStore(self, ec, pRange, pPropStore):
##        '-no docstring-'
##        #return 
##
##    def SetValue(self, ec, pRange, pvarValue):
##        '-no docstring-'
##        #return 
##

wireASYNC_STGMEDIUM = POINTER(_userSTGMEDIUM)
IAdviseSink._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteOnDataChange',
              ( ['in'], POINTER(tagFORMATETC), 'pformatetc' ),
              ( ['in'], POINTER(wireASYNC_STGMEDIUM), 'pStgmed' )),
    COMMETHOD([], HRESULT, 'RemoteOnViewChange',
              ( ['in'], c_ulong, 'dwAspect' ),
              ( ['in'], c_int, 'lindex' )),
    COMMETHOD([], HRESULT, 'RemoteOnRename',
              ( ['in'], POINTER(IMoniker), 'pmk' )),
    COMMETHOD([], HRESULT, 'RemoteOnSave'),
    COMMETHOD([], HRESULT, 'RemoteOnClose'),
]
################################################################
## code template for IAdviseSink implementation
##class IAdviseSink_Impl(object):
##    def RemoteOnViewChange(self, dwAspect, lindex):
##        '-no docstring-'
##        #return 
##
##    def RemoteOnRename(self, pmk):
##        '-no docstring-'
##        #return 
##
##    def RemoteOnSave(self):
##        '-no docstring-'
##        #return 
##
##    def RemoteOnDataChange(self, pformatetc, pStgmed):
##        '-no docstring-'
##        #return 
##
##    def RemoteOnClose(self):
##        '-no docstring-'
##        #return 
##

class ISequentialStream(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{0C733A30-2A1C-11CE-ADE5-00AA0044773D}')
    _idlflags_ = []
class IStream(ISequentialStream):
    _case_insensitive_ = True
    _iid_ = GUID('{0000000C-0000-0000-C000-000000000046}')
    _idlflags_ = []
IPersistStream._methods_ = [
    COMMETHOD([], HRESULT, 'IsDirty'),
    COMMETHOD([], HRESULT, 'Load',
              ( ['in'], POINTER(IStream), 'pstm' )),
    COMMETHOD([], HRESULT, 'Save',
              ( ['in'], POINTER(IStream), 'pstm' ),
              ( ['in'], c_int, 'fClearDirty' )),
    COMMETHOD([], HRESULT, 'GetSizeMax',
              ( ['out'], POINTER(_ULARGE_INTEGER), 'pcbSize' )),
]
################################################################
## code template for IPersistStream implementation
##class IPersistStream_Impl(object):
##    def Load(self, pstm):
##        '-no docstring-'
##        #return 
##
##    def GetSizeMax(self):
##        '-no docstring-'
##        #return pcbSize
##
##    def Save(self, pstm, fClearDirty):
##        '-no docstring-'
##        #return 
##
##    def IsDirty(self):
##        '-no docstring-'
##        #return 
##

class IBindCtx(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{0000000E-0000-0000-C000-000000000046}')
    _idlflags_ = []
IMoniker._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteBindToObject',
              ( ['in'], POINTER(IBindCtx), 'pbc' ),
              ( ['in'], POINTER(IMoniker), 'pmkToLeft' ),
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'riidResult' ),
              ( ['out'], POINTER(POINTER(IUnknown)), 'ppvResult' )),
    COMMETHOD([], HRESULT, 'RemoteBindToStorage',
              ( ['in'], POINTER(IBindCtx), 'pbc' ),
              ( ['in'], POINTER(IMoniker), 'pmkToLeft' ),
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'riid' ),
              ( ['out'], POINTER(POINTER(IUnknown)), 'ppvObj' )),
    COMMETHOD([], HRESULT, 'Reduce',
              ( ['in'], POINTER(IBindCtx), 'pbc' ),
              ( ['in'], c_ulong, 'dwReduceHowFar' ),
              ( ['in', 'out'], POINTER(POINTER(IMoniker)), 'ppmkToLeft' ),
              ( ['out'], POINTER(POINTER(IMoniker)), 'ppmkReduced' )),
    COMMETHOD([], HRESULT, 'ComposeWith',
              ( ['in'], POINTER(IMoniker), 'pmkRight' ),
              ( ['in'], c_int, 'fOnlyIfNotGeneric' ),
              ( ['out'], POINTER(POINTER(IMoniker)), 'ppmkComposite' )),
    COMMETHOD([], HRESULT, 'Enum',
              ( ['in'], c_int, 'fForward' ),
              ( ['out'], POINTER(POINTER(IEnumMoniker)), 'ppenumMoniker' )),
    COMMETHOD([], HRESULT, 'IsEqual',
              ( ['in'], POINTER(IMoniker), 'pmkOtherMoniker' )),
    COMMETHOD([], HRESULT, 'Hash',
              ( ['out'], POINTER(c_ulong), 'pdwHash' )),
    COMMETHOD([], HRESULT, 'IsRunning',
              ( ['in'], POINTER(IBindCtx), 'pbc' ),
              ( ['in'], POINTER(IMoniker), 'pmkToLeft' ),
              ( ['in'], POINTER(IMoniker), 'pmkNewlyRunning' )),
    COMMETHOD([], HRESULT, 'GetTimeOfLastChange',
              ( ['in'], POINTER(IBindCtx), 'pbc' ),
              ( ['in'], POINTER(IMoniker), 'pmkToLeft' ),
              ( ['out'], POINTER(_FILETIME), 'pfiletime' )),
    COMMETHOD([], HRESULT, 'Inverse',
              ( ['out'], POINTER(POINTER(IMoniker)), 'ppmk' )),
    COMMETHOD([], HRESULT, 'CommonPrefixWith',
              ( ['in'], POINTER(IMoniker), 'pmkOther' ),
              ( ['out'], POINTER(POINTER(IMoniker)), 'ppmkPrefix' )),
    COMMETHOD([], HRESULT, 'RelativePathTo',
              ( ['in'], POINTER(IMoniker), 'pmkOther' ),
              ( ['out'], POINTER(POINTER(IMoniker)), 'ppmkRelPath' )),
    COMMETHOD([], HRESULT, 'GetDisplayName',
              ( ['in'], POINTER(IBindCtx), 'pbc' ),
              ( ['in'], POINTER(IMoniker), 'pmkToLeft' ),
              ( ['out'], POINTER(WSTRING), 'ppszDisplayName' )),
    COMMETHOD([], HRESULT, 'ParseDisplayName',
              ( ['in'], POINTER(IBindCtx), 'pbc' ),
              ( ['in'], POINTER(IMoniker), 'pmkToLeft' ),
              ( ['in'], WSTRING, 'pszDisplayName' ),
              ( ['out'], POINTER(c_ulong), 'pchEaten' ),
              ( ['out'], POINTER(POINTER(IMoniker)), 'ppmkOut' )),
    COMMETHOD([], HRESULT, 'IsSystemMoniker',
              ( ['out'], POINTER(c_ulong), 'pdwMksys' )),
]
################################################################
## code template for IMoniker implementation
##class IMoniker_Impl(object):
##    def RelativePathTo(self, pmkOther):
##        '-no docstring-'
##        #return ppmkRelPath
##
##    def GetTimeOfLastChange(self, pbc, pmkToLeft):
##        '-no docstring-'
##        #return pfiletime
##
##    def ComposeWith(self, pmkRight, fOnlyIfNotGeneric):
##        '-no docstring-'
##        #return ppmkComposite
##
##    def Hash(self):
##        '-no docstring-'
##        #return pdwHash
##
##    def IsSystemMoniker(self):
##        '-no docstring-'
##        #return pdwMksys
##
##    def ParseDisplayName(self, pbc, pmkToLeft, pszDisplayName):
##        '-no docstring-'
##        #return pchEaten, ppmkOut
##
##    def RemoteBindToStorage(self, pbc, pmkToLeft, riid):
##        '-no docstring-'
##        #return ppvObj
##
##    def Enum(self, fForward):
##        '-no docstring-'
##        #return ppenumMoniker
##
##    def Reduce(self, pbc, dwReduceHowFar):
##        '-no docstring-'
##        #return ppmkToLeft, ppmkReduced
##
##    def Inverse(self):
##        '-no docstring-'
##        #return ppmk
##
##    def RemoteBindToObject(self, pbc, pmkToLeft, riidResult):
##        '-no docstring-'
##        #return ppvResult
##
##    def IsEqual(self, pmkOtherMoniker):
##        '-no docstring-'
##        #return 
##
##    def IsRunning(self, pbc, pmkToLeft, pmkNewlyRunning):
##        '-no docstring-'
##        #return 
##
##    def CommonPrefixWith(self, pmkOther):
##        '-no docstring-'
##        #return ppmkPrefix
##
##    def GetDisplayName(self, pbc, pmkToLeft):
##        '-no docstring-'
##        #return ppszDisplayName
##

class Library(object):
    name = u'BoGo'
    _reg_typelib_ = ('{C4E07FAB-27D8-45C1-A647-DB6D4F590C31}', 0, 0)

IEnumMoniker._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteNext',
              ( ['in'], c_ulong, 'celt' ),
              ( ['out'], POINTER(POINTER(IMoniker)), 'rgelt' ),
              ( ['out'], POINTER(c_ulong), 'pceltFetched' )),
    COMMETHOD([], HRESULT, 'Skip',
              ( ['in'], c_ulong, 'celt' )),
    COMMETHOD([], HRESULT, 'Reset'),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IEnumMoniker)), 'ppenum' )),
]
################################################################
## code template for IEnumMoniker implementation
##class IEnumMoniker_Impl(object):
##    def Reset(self):
##        '-no docstring-'
##        #return 
##
##    def Skip(self, celt):
##        '-no docstring-'
##        #return 
##
##    def Clone(self):
##        '-no docstring-'
##        #return ppenum
##
##    def RemoteNext(self, celt):
##        '-no docstring-'
##        #return rgelt, pceltFetched
##

class ITfContextView(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{2433BF8E-0F9B-435C-BA2C-180611978C30}')
    _idlflags_ = []
ITfContextView._methods_ = [
    COMMETHOD([], HRESULT, 'GetRangeFromPoint',
              ( ['in'], TfEditCookie, 'ec' ),
              ( ['in'], POINTER(tagPOINT), 'ppt' ),
              ( ['in'], c_ulong, 'dwFlags' ),
              ( ['out'], POINTER(POINTER(ITfRange)), 'ppRange' )),
    COMMETHOD([], HRESULT, 'GetTextExt',
              ( ['in'], TfEditCookie, 'ec' ),
              ( ['in'], POINTER(ITfRange), 'pRange' ),
              ( ['out'], POINTER(tagRECT), 'prc' ),
              ( ['out'], POINTER(c_int), 'pfClipped' )),
    COMMETHOD([], HRESULT, 'GetScreenExt',
              ( ['out'], POINTER(tagRECT), 'prc' )),
    COMMETHOD([], HRESULT, 'GetWnd',
              ( ['out'], POINTER(wireHWND), 'phwnd' )),
]
################################################################
## code template for ITfContextView implementation
##class ITfContextView_Impl(object):
##    def GetTextExt(self, ec, pRange):
##        '-no docstring-'
##        #return prc, pfClipped
##
##    def GetScreenExt(self):
##        '-no docstring-'
##        #return prc
##
##    def GetRangeFromPoint(self, ec, ppt, dwFlags):
##        '-no docstring-'
##        #return ppRange
##
##    def GetWnd(self):
##        '-no docstring-'
##        #return phwnd
##

class __MIDL_IWinTypes_0005(Union):
    pass
class _remoteMETAFILEPICT(Structure):
    pass
__MIDL_IWinTypes_0005._fields_ = [
    ('hInproc', c_int),
    ('hRemote', POINTER(_remoteMETAFILEPICT)),
    ('hInproc64', c_longlong),
]
assert sizeof(__MIDL_IWinTypes_0005) == 8, sizeof(__MIDL_IWinTypes_0005)
assert alignment(__MIDL_IWinTypes_0005) == 8, alignment(__MIDL_IWinTypes_0005)
_userHMETAFILEPICT._fields_ = [
    ('fContext', c_int),
    ('u', __MIDL_IWinTypes_0005),
]
assert sizeof(_userHMETAFILEPICT) == 16, sizeof(_userHMETAFILEPICT)
assert alignment(_userHMETAFILEPICT) == 8, alignment(_userHMETAFILEPICT)
ISequentialStream._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteRead',
              ( ['out'], POINTER(c_ubyte), 'pv' ),
              ( ['in'], c_ulong, 'cb' ),
              ( ['out'], POINTER(c_ulong), 'pcbRead' )),
    COMMETHOD([], HRESULT, 'RemoteWrite',
              ( ['in'], POINTER(c_ubyte), 'pv' ),
              ( ['in'], c_ulong, 'cb' ),
              ( ['out'], POINTER(c_ulong), 'pcbWritten' )),
]
################################################################
## code template for ISequentialStream implementation
##class ISequentialStream_Impl(object):
##    def RemoteRead(self, cb):
##        '-no docstring-'
##        #return pv, pcbRead
##
##    def RemoteWrite(self, pv, cb):
##        '-no docstring-'
##        #return pcbWritten
##

class tagSTATSTG(Structure):
    pass
IStream._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteSeek',
              ( ['in'], _LARGE_INTEGER, 'dlibMove' ),
              ( ['in'], c_ulong, 'dwOrigin' ),
              ( ['out'], POINTER(_ULARGE_INTEGER), 'plibNewPosition' )),
    COMMETHOD([], HRESULT, 'SetSize',
              ( ['in'], _ULARGE_INTEGER, 'libNewSize' )),
    COMMETHOD([], HRESULT, 'RemoteCopyTo',
              ( ['in'], POINTER(IStream), 'pstm' ),
              ( ['in'], _ULARGE_INTEGER, 'cb' ),
              ( ['out'], POINTER(_ULARGE_INTEGER), 'pcbRead' ),
              ( ['out'], POINTER(_ULARGE_INTEGER), 'pcbWritten' )),
    COMMETHOD([], HRESULT, 'Commit',
              ( ['in'], c_ulong, 'grfCommitFlags' )),
    COMMETHOD([], HRESULT, 'Revert'),
    COMMETHOD([], HRESULT, 'LockRegion',
              ( ['in'], _ULARGE_INTEGER, 'libOffset' ),
              ( ['in'], _ULARGE_INTEGER, 'cb' ),
              ( ['in'], c_ulong, 'dwLockType' )),
    COMMETHOD([], HRESULT, 'UnlockRegion',
              ( ['in'], _ULARGE_INTEGER, 'libOffset' ),
              ( ['in'], _ULARGE_INTEGER, 'cb' ),
              ( ['in'], c_ulong, 'dwLockType' )),
    COMMETHOD([], HRESULT, 'Stat',
              ( ['out'], POINTER(tagSTATSTG), 'pstatstg' ),
              ( ['in'], c_ulong, 'grfStatFlag' )),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IStream)), 'ppstm' )),
]
################################################################
## code template for IStream implementation
##class IStream_Impl(object):
##    def RemoteSeek(self, dlibMove, dwOrigin):
##        '-no docstring-'
##        #return plibNewPosition
##
##    def Stat(self, grfStatFlag):
##        '-no docstring-'
##        #return pstatstg
##
##    def UnlockRegion(self, libOffset, cb, dwLockType):
##        '-no docstring-'
##        #return 
##
##    def Clone(self):
##        '-no docstring-'
##        #return ppstm
##
##    def Revert(self):
##        '-no docstring-'
##        #return 
##
##    def RemoteCopyTo(self, pstm, cb):
##        '-no docstring-'
##        #return pcbRead, pcbWritten
##
##    def LockRegion(self, libOffset, cb, dwLockType):
##        '-no docstring-'
##        #return 
##
##    def Commit(self, grfCommitFlags):
##        '-no docstring-'
##        #return 
##
##    def SetSize(self, libNewSize):
##        '-no docstring-'
##        #return 
##

class BoGo(CoClass):
    _reg_clsid_ = GUID('{4581A23E-03EA-4614-975B-FF6206A8B840}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C4E07FAB-27D8-45C1-A647-DB6D4F590C31}', 0, 0)
class ITfTextInputProcessor(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{AA80E7F7-2021-11D2-93E0-0060B067B86E}')
    _idlflags_ = []
BoGo._com_interfaces_ = [ITfTextInputProcessor, comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch]

ITfPropertyStore._methods_ = [
    COMMETHOD([], HRESULT, 'GetType',
              ( ['out'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'pguid' )),
    COMMETHOD([], HRESULT, 'GetDataType',
              ( ['out'], POINTER(c_ulong), 'pdwReserved' )),
    COMMETHOD([], HRESULT, 'GetData',
              ( ['out'], POINTER(VARIANT), 'pvarValue' )),
    COMMETHOD([], HRESULT, 'OnTextUpdated',
              ( ['in'], c_ulong, 'dwFlags' ),
              ( ['in'], POINTER(ITfRange), 'pRangeNew' ),
              ( ['out'], POINTER(c_int), 'pfAccept' )),
    COMMETHOD([], HRESULT, 'Shrink',
              ( ['in'], POINTER(ITfRange), 'pRangeNew' ),
              ( ['out'], POINTER(c_int), 'pfFree' )),
    COMMETHOD([], HRESULT, 'Divide',
              ( ['in'], POINTER(ITfRange), 'pRangeThis' ),
              ( ['in'], POINTER(ITfRange), 'pRangeNew' ),
              ( ['out'], POINTER(POINTER(ITfPropertyStore)), 'ppPropStore' )),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(ITfPropertyStore)), 'pPropStore' )),
    COMMETHOD([], HRESULT, 'GetPropertyRangeCreator',
              ( ['out'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'pclsid' )),
    COMMETHOD([], HRESULT, 'Serialize',
              ( ['in'], POINTER(IStream), 'pStream' ),
              ( ['out'], POINTER(c_ulong), 'pcb' )),
]
################################################################
## code template for ITfPropertyStore implementation
##class ITfPropertyStore_Impl(object):
##    def Serialize(self, pStream):
##        '-no docstring-'
##        #return pcb
##
##    def Divide(self, pRangeThis, pRangeNew):
##        '-no docstring-'
##        #return ppPropStore
##
##    def Clone(self):
##        '-no docstring-'
##        #return pPropStore
##
##    def GetType(self):
##        '-no docstring-'
##        #return pguid
##
##    def GetPropertyRangeCreator(self):
##        '-no docstring-'
##        #return pclsid
##
##    def OnTextUpdated(self, dwFlags, pRangeNew):
##        '-no docstring-'
##        #return pfAccept
##
##    def GetData(self):
##        '-no docstring-'
##        #return pvarValue
##
##    def Shrink(self, pRangeNew):
##        '-no docstring-'
##        #return pfFree
##
##    def GetDataType(self):
##        '-no docstring-'
##        #return pdwReserved
##

class ITfThreadMgr(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{AA80E801-2021-11D2-93E0-0060B067B86E}')
    _idlflags_ = []
ITfTextInputProcessor._methods_ = [
    COMMETHOD([], HRESULT, 'Activate',
              ( ['in'], POINTER(ITfThreadMgr), 'ptim' ),
              ( ['in'], TfClientId, 'tid' )),
    COMMETHOD([], HRESULT, 'Deactivate'),
]
################################################################
## code template for ITfTextInputProcessor implementation
##class ITfTextInputProcessor_Impl(object):
##    def Deactivate(self):
##        '-no docstring-'
##        #return 
##
##    def Activate(self, ptim, tid):
##        '-no docstring-'
##        #return 
##

class TF_HALTCOND(Structure):
    _recordinfo_ = ('{C4E07FAB-27D8-45C1-A647-DB6D4F590C31}', 0, 0, 0L, '{49930D51-7D93-448C-A48C-FEA5DAC192B1}')
TF_HALTCOND._fields_ = [
    ('pHaltRange', POINTER(ITfRange)),
    ('aHaltPos', TfAnchor),
    ('dwFlags', c_ulong),
]
assert sizeof(TF_HALTCOND) == 12, sizeof(TF_HALTCOND)
assert alignment(TF_HALTCOND) == 4, alignment(TF_HALTCOND)
_remoteMETAFILEPICT._fields_ = [
    ('mm', c_int),
    ('xExt', c_int),
    ('yExt', c_int),
    ('hMF', POINTER(_userHMETAFILE)),
]
assert sizeof(_remoteMETAFILEPICT) == 16, sizeof(_remoteMETAFILEPICT)
assert alignment(_remoteMETAFILEPICT) == 4, alignment(_remoteMETAFILEPICT)
class __MIDL_IWinTypes_0006(Union):
    pass
__MIDL_IWinTypes_0006._fields_ = [
    ('hInproc', c_int),
    ('hRemote', POINTER(_BYTE_BLOB)),
    ('hInproc64', c_longlong),
]
assert sizeof(__MIDL_IWinTypes_0006) == 8, sizeof(__MIDL_IWinTypes_0006)
assert alignment(__MIDL_IWinTypes_0006) == 8, alignment(__MIDL_IWinTypes_0006)
_userHENHMETAFILE._fields_ = [
    ('fContext', c_int),
    ('u', __MIDL_IWinTypes_0006),
]
assert sizeof(_userHENHMETAFILE) == 16, sizeof(_userHENHMETAFILE)
assert alignment(_userHENHMETAFILE) == 8, alignment(_userHENHMETAFILE)
class ITfFunctionProvider(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{101D6610-0990-11D3-8DF0-00105A2799B5}')
    _idlflags_ = []
ITfFunctionProvider._methods_ = [
    COMMETHOD([], HRESULT, 'GetType',
              ( ['out'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'pguid' )),
    COMMETHOD([], HRESULT, 'GetDescription',
              ( ['out'], POINTER(BSTR), 'pbstrDesc' )),
    COMMETHOD([], HRESULT, 'GetFunction',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'rguid' ),
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'riid' ),
              ( ['out'], POINTER(POINTER(IUnknown)), 'ppunk' )),
]
################################################################
## code template for ITfFunctionProvider implementation
##class ITfFunctionProvider_Impl(object):
##    def GetType(self):
##        '-no docstring-'
##        #return pguid
##
##    def GetDescription(self):
##        '-no docstring-'
##        #return pbstrDesc
##
##    def GetFunction(self, rguid, riid):
##        '-no docstring-'
##        #return ppunk
##

class ITfDocumentMgr(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{AA80E7F4-2021-11D2-93E0-0060B067B86E}')
    _idlflags_ = []
class IEnumTfDocumentMgrs(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{AA80E808-2021-11D2-93E0-0060B067B86E}')
    _idlflags_ = []
    def __iter__(self):
        return self

    def next(self):
        item, fetched = self.Next(1)
        if fetched:
            return item
        raise StopIteration

    def __getitem__(self, index):
        self.Reset()
        self.Skip(index)
        item, fetched = self.Next(1)
        if fetched:
            return item
        raise IndexError(index)

class IEnumTfFunctionProviders(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{E4B24DB0-0990-11D3-8DF0-00105A2799B5}')
    _idlflags_ = []
    def __iter__(self):
        return self

    def next(self):
        item, fetched = self.Next(1)
        if fetched:
            return item
        raise StopIteration

    def __getitem__(self, index):
        self.Reset()
        self.Skip(index)
        item, fetched = self.Next(1)
        if fetched:
            return item
        raise IndexError(index)

class ITfCompartmentMgr(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{7DCF57AC-18AD-438B-824D-979BFFB74B7C}')
    _idlflags_ = []
ITfThreadMgr._methods_ = [
    COMMETHOD([], HRESULT, 'Activate',
              ( ['out'], POINTER(TfClientId), 'ptid' )),
    COMMETHOD([], HRESULT, 'Deactivate'),
    COMMETHOD([], HRESULT, 'CreateDocumentMgr',
              ( ['out'], POINTER(POINTER(ITfDocumentMgr)), 'ppdim' )),
    COMMETHOD([], HRESULT, 'EnumDocumentMgrs',
              ( ['out'], POINTER(POINTER(IEnumTfDocumentMgrs)), 'ppenum' )),
    COMMETHOD([], HRESULT, 'GetFocus',
              ( ['out'], POINTER(POINTER(ITfDocumentMgr)), 'ppdimFocus' )),
    COMMETHOD([], HRESULT, 'SetFocus',
              ( ['in'], POINTER(ITfDocumentMgr), 'pdimFocus' )),
    COMMETHOD([], HRESULT, 'AssociateFocus',
              ( ['in'], wireHWND, 'hwnd' ),
              ( ['in'], POINTER(ITfDocumentMgr), 'pdimNew' ),
              ( ['out'], POINTER(POINTER(ITfDocumentMgr)), 'ppdimPrev' )),
    COMMETHOD([], HRESULT, 'IsThreadFocus',
              ( ['out'], POINTER(c_int), 'pfThreadFocus' )),
    COMMETHOD([], HRESULT, 'GetFunctionProvider',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'clsid' ),
              ( ['out'], POINTER(POINTER(ITfFunctionProvider)), 'ppFuncProv' )),
    COMMETHOD([], HRESULT, 'EnumFunctionProviders',
              ( ['out'], POINTER(POINTER(IEnumTfFunctionProviders)), 'ppenum' )),
    COMMETHOD([], HRESULT, 'GetGlobalCompartment',
              ( ['out'], POINTER(POINTER(ITfCompartmentMgr)), 'ppCompMgr' )),
]
################################################################
## code template for ITfThreadMgr implementation
##class ITfThreadMgr_Impl(object):
##    def SetFocus(self, pdimFocus):
##        '-no docstring-'
##        #return 
##
##    def Activate(self):
##        '-no docstring-'
##        #return ptid
##
##    def AssociateFocus(self, hwnd, pdimNew):
##        '-no docstring-'
##        #return ppdimPrev
##
##    def Deactivate(self):
##        '-no docstring-'
##        #return 
##
##    def EnumDocumentMgrs(self):
##        '-no docstring-'
##        #return ppenum
##
##    def GetGlobalCompartment(self):
##        '-no docstring-'
##        #return ppCompMgr
##
##    def IsThreadFocus(self):
##        '-no docstring-'
##        #return pfThreadFocus
##
##    def CreateDocumentMgr(self):
##        '-no docstring-'
##        #return ppdim
##
##    def GetFunctionProvider(self, clsid):
##        '-no docstring-'
##        #return ppFuncProv
##
##    def GetFocus(self):
##        '-no docstring-'
##        #return ppdimFocus
##
##    def EnumFunctionProviders(self):
##        '-no docstring-'
##        #return ppenum
##

class __MIDL_IAdviseSink_0002(Union):
    pass
class _userHBITMAP(Structure):
    pass
class _userHPALETTE(Structure):
    pass
__MIDL_IAdviseSink_0002._fields_ = [
    ('hBitmap', POINTER(_userHBITMAP)),
    ('hPalette', POINTER(_userHPALETTE)),
    ('hGeneric', POINTER(_userHGLOBAL)),
]
assert sizeof(__MIDL_IAdviseSink_0002) == 4, sizeof(__MIDL_IAdviseSink_0002)
assert alignment(__MIDL_IAdviseSink_0002) == 4, alignment(__MIDL_IAdviseSink_0002)
_GDI_OBJECT._fields_ = [
    ('ObjectType', c_ulong),
    ('u', __MIDL_IAdviseSink_0002),
]
assert sizeof(_GDI_OBJECT) == 8, sizeof(_GDI_OBJECT)
assert alignment(_GDI_OBJECT) == 4, alignment(_GDI_OBJECT)
class tagSTATDATA(Structure):
    pass
tagSTATDATA._fields_ = [
    ('formatetc', tagFORMATETC),
    ('advf', c_ulong),
    ('pAdvSink', POINTER(IAdviseSink)),
    ('dwConnection', c_ulong),
]
assert sizeof(tagSTATDATA) == 32, sizeof(tagSTATDATA)
assert alignment(tagSTATDATA) == 4, alignment(tagSTATDATA)
tagDVTARGETDEVICE._fields_ = [
    ('tdSize', c_ulong),
    ('tdDriverNameOffset', c_ushort),
    ('tdDeviceNameOffset', c_ushort),
    ('tdPortNameOffset', c_ushort),
    ('tdExtDevmodeOffset', c_ushort),
    ('tdData', POINTER(c_ubyte)),
]
assert sizeof(tagDVTARGETDEVICE) == 16, sizeof(tagDVTARGETDEVICE)
assert alignment(tagDVTARGETDEVICE) == 4, alignment(tagDVTARGETDEVICE)
_BYTE_BLOB._fields_ = [
    ('clSize', c_ulong),
    ('abData', POINTER(c_ubyte)),
]
assert sizeof(_BYTE_BLOB) == 8, sizeof(_BYTE_BLOB)
assert alignment(_BYTE_BLOB) == 4, alignment(_BYTE_BLOB)

# values for enumeration '__MIDL_ITfRange_0002'
TF_SD_BACKWARD = 0
TF_SD_FORWARD = 1
__MIDL_ITfRange_0002 = c_int # enum
TfShiftDir = __MIDL_ITfRange_0002

# values for enumeration '__MIDL_ITfRange_0001'
TF_GRAVITY_BACKWARD = 0
TF_GRAVITY_FORWARD = 1
__MIDL_ITfRange_0001 = c_int # enum
TfGravity = __MIDL_ITfRange_0001
ITfRange._methods_ = [
    COMMETHOD([], HRESULT, 'GetText',
              ( ['in'], TfEditCookie, 'ec' ),
              ( ['in'], c_ulong, 'dwFlags' ),
              ( ['out'], POINTER(c_ushort), 'pchText' ),
              ( ['in'], c_ulong, 'cchMax' ),
              ( ['out'], POINTER(c_ulong), 'pcch' )),
    COMMETHOD([], HRESULT, 'SetText',
              ( ['in'], TfEditCookie, 'ec' ),
              ( ['in'], c_ulong, 'dwFlags' ),
              ( ['in'], POINTER(c_ushort), 'pchText' ),
              ( ['in'], c_int, 'cch' )),
    COMMETHOD([], HRESULT, 'GetFormattedText',
              ( ['in'], TfEditCookie, 'ec' ),
              ( ['out'], POINTER(POINTER(IDataObject)), 'ppDataObject' )),
    COMMETHOD([], HRESULT, 'GetEmbedded',
              ( ['in'], TfEditCookie, 'ec' ),
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'rguidService' ),
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'riid' ),
              ( ['out'], POINTER(POINTER(IUnknown)), 'ppunk' )),
    COMMETHOD([], HRESULT, 'InsertEmbedded',
              ( ['in'], TfEditCookie, 'ec' ),
              ( ['in'], c_ulong, 'dwFlags' ),
              ( ['in'], POINTER(IDataObject), 'pDataObject' )),
    COMMETHOD([], HRESULT, 'ShiftStart',
              ( ['in'], TfEditCookie, 'ec' ),
              ( ['in'], c_int, 'cchReq' ),
              ( ['out'], POINTER(c_int), 'pcch' ),
              ( ['in'], POINTER(TF_HALTCOND), 'pHalt' )),
    COMMETHOD([], HRESULT, 'ShiftEnd',
              ( ['in'], TfEditCookie, 'ec' ),
              ( ['in'], c_int, 'cchReq' ),
              ( ['out'], POINTER(c_int), 'pcch' ),
              ( ['in'], POINTER(TF_HALTCOND), 'pHalt' )),
    COMMETHOD([], HRESULT, 'ShiftStartToRange',
              ( ['in'], TfEditCookie, 'ec' ),
              ( ['in'], POINTER(ITfRange), 'pRange' ),
              ( ['in'], TfAnchor, 'aPos' )),
    COMMETHOD([], HRESULT, 'ShiftEndToRange',
              ( ['in'], TfEditCookie, 'ec' ),
              ( ['in'], POINTER(ITfRange), 'pRange' ),
              ( ['in'], TfAnchor, 'aPos' )),
    COMMETHOD([], HRESULT, 'ShiftStartRegion',
              ( ['in'], TfEditCookie, 'ec' ),
              ( ['in'], TfShiftDir, 'dir' ),
              ( ['out'], POINTER(c_int), 'pfNoRegion' )),
    COMMETHOD([], HRESULT, 'ShiftEndRegion',
              ( ['in'], TfEditCookie, 'ec' ),
              ( ['in'], TfShiftDir, 'dir' ),
              ( ['out'], POINTER(c_int), 'pfNoRegion' )),
    COMMETHOD([], HRESULT, 'IsEmpty',
              ( ['in'], TfEditCookie, 'ec' ),
              ( ['out'], POINTER(c_int), 'pfEmpty' )),
    COMMETHOD([], HRESULT, 'Collapse',
              ( ['in'], TfEditCookie, 'ec' ),
              ( ['in'], TfAnchor, 'aPos' )),
    COMMETHOD([], HRESULT, 'IsEqualStart',
              ( ['in'], TfEditCookie, 'ec' ),
              ( ['in'], POINTER(ITfRange), 'pWith' ),
              ( ['in'], TfAnchor, 'aPos' ),
              ( ['out'], POINTER(c_int), 'pfEqual' )),
    COMMETHOD([], HRESULT, 'IsEqualEnd',
              ( ['in'], TfEditCookie, 'ec' ),
              ( ['in'], POINTER(ITfRange), 'pWith' ),
              ( ['in'], TfAnchor, 'aPos' ),
              ( ['out'], POINTER(c_int), 'pfEqual' )),
    COMMETHOD([], HRESULT, 'CompareStart',
              ( ['in'], TfEditCookie, 'ec' ),
              ( ['in'], POINTER(ITfRange), 'pWith' ),
              ( ['in'], TfAnchor, 'aPos' ),
              ( ['out'], POINTER(c_int), 'plResult' )),
    COMMETHOD([], HRESULT, 'CompareEnd',
              ( ['in'], TfEditCookie, 'ec' ),
              ( ['in'], POINTER(ITfRange), 'pWith' ),
              ( ['in'], TfAnchor, 'aPos' ),
              ( ['out'], POINTER(c_int), 'plResult' )),
    COMMETHOD([], HRESULT, 'AdjustForInsert',
              ( ['in'], TfEditCookie, 'ec' ),
              ( ['in'], c_ulong, 'cchInsert' ),
              ( ['out'], POINTER(c_int), 'pfInsertOk' )),
    COMMETHOD([], HRESULT, 'GetGravity',
              ( ['out'], POINTER(TfGravity), 'pgStart' ),
              ( ['out'], POINTER(TfGravity), 'pgEnd' )),
    COMMETHOD([], HRESULT, 'SetGravity',
              ( ['in'], TfEditCookie, 'ec' ),
              ( ['in'], TfGravity, 'gStart' ),
              ( ['in'], TfGravity, 'gEnd' )),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(ITfRange)), 'ppClone' )),
    COMMETHOD([], HRESULT, 'GetContext',
              ( ['out'], POINTER(POINTER(ITfContext)), 'ppContext' )),
]
################################################################
## code template for ITfRange implementation
##class ITfRange_Impl(object):
##    def SetText(self, ec, dwFlags, pchText, cch):
##        '-no docstring-'
##        #return 
##
##    def InsertEmbedded(self, ec, dwFlags, pDataObject):
##        '-no docstring-'
##        #return 
##
##    def AdjustForInsert(self, ec, cchInsert):
##        '-no docstring-'
##        #return pfInsertOk
##
##    def ShiftStartToRange(self, ec, pRange, aPos):
##        '-no docstring-'
##        #return 
##
##    def SetGravity(self, ec, gStart, gEnd):
##        '-no docstring-'
##        #return 
##
##    def Collapse(self, ec, aPos):
##        '-no docstring-'
##        #return 
##
##    def Clone(self):
##        '-no docstring-'
##        #return ppClone
##
##    def GetText(self, ec, dwFlags, cchMax):
##        '-no docstring-'
##        #return pchText, pcch
##
##    def GetContext(self):
##        '-no docstring-'
##        #return ppContext
##
##    def ShiftStart(self, ec, cchReq, pHalt):
##        '-no docstring-'
##        #return pcch
##
##    def CompareStart(self, ec, pWith, aPos):
##        '-no docstring-'
##        #return plResult
##
##    def IsEqualStart(self, ec, pWith, aPos):
##        '-no docstring-'
##        #return pfEqual
##
##    def ShiftEnd(self, ec, cchReq, pHalt):
##        '-no docstring-'
##        #return pcch
##
##    def IsEmpty(self, ec):
##        '-no docstring-'
##        #return pfEmpty
##
##    def GetFormattedText(self, ec):
##        '-no docstring-'
##        #return ppDataObject
##
##    def CompareEnd(self, ec, pWith, aPos):
##        '-no docstring-'
##        #return plResult
##
##    def ShiftEndToRange(self, ec, pRange, aPos):
##        '-no docstring-'
##        #return 
##
##    def ShiftStartRegion(self, ec, dir):
##        '-no docstring-'
##        #return pfNoRegion
##
##    def GetEmbedded(self, ec, rguidService, riid):
##        '-no docstring-'
##        #return ppunk
##
##    def GetGravity(self):
##        '-no docstring-'
##        #return pgStart, pgEnd
##
##    def IsEqualEnd(self, ec, pWith, aPos):
##        '-no docstring-'
##        #return pfEqual
##
##    def ShiftEndRegion(self, ec, dir):
##        '-no docstring-'
##        #return pfNoRegion
##

tagSTATSTG._fields_ = [
    ('pwcsName', WSTRING),
    ('type', c_ulong),
    ('cbSize', _ULARGE_INTEGER),
    ('mtime', _FILETIME),
    ('ctime', _FILETIME),
    ('atime', _FILETIME),
    ('grfMode', c_ulong),
    ('grfLocksSupported', c_ulong),
    ('clsid', comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID),
    ('grfStateBits', c_ulong),
    ('reserved', c_ulong),
]
assert sizeof(tagSTATSTG) == 72, sizeof(tagSTATSTG)
assert alignment(tagSTATSTG) == 8, alignment(tagSTATSTG)
class _RemotableHandle(Structure):
    pass
class __MIDL_IWinTypes_0009(Union):
    pass
__MIDL_IWinTypes_0009._fields_ = [
    ('hInproc', c_int),
    ('hRemote', c_int),
]
assert sizeof(__MIDL_IWinTypes_0009) == 4, sizeof(__MIDL_IWinTypes_0009)
assert alignment(__MIDL_IWinTypes_0009) == 4, alignment(__MIDL_IWinTypes_0009)
_RemotableHandle._fields_ = [
    ('fContext', c_int),
    ('u', __MIDL_IWinTypes_0009),
]
assert sizeof(_RemotableHandle) == 8, sizeof(_RemotableHandle)
assert alignment(_RemotableHandle) == 4, alignment(_RemotableHandle)
IEnumTfFunctionProviders._methods_ = [
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IEnumTfFunctionProviders)), 'ppenum' )),
    COMMETHOD([], HRESULT, 'Next',
              ( ['in'], c_ulong, 'ulCount' ),
              ( ['out'], POINTER(POINTER(ITfFunctionProvider)), 'ppCmdobj' ),
              ( ['out'], POINTER(c_ulong), 'pcFetch' )),
    COMMETHOD([], HRESULT, 'Reset'),
    COMMETHOD([], HRESULT, 'Skip',
              ( ['in'], c_ulong, 'ulCount' )),
]
################################################################
## code template for IEnumTfFunctionProviders implementation
##class IEnumTfFunctionProviders_Impl(object):
##    def Reset(self):
##        '-no docstring-'
##        #return 
##
##    def Skip(self, ulCount):
##        '-no docstring-'
##        #return 
##
##    def Clone(self):
##        '-no docstring-'
##        #return ppenum
##
##    def Next(self, ulCount):
##        '-no docstring-'
##        #return ppCmdobj, pcFetch
##

class IEnumTfContextViews(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{F0C0F8DD-CF38-44E1-BB0F-68CF0D551C78}')
    _idlflags_ = []
    def __iter__(self):
        return self

    def next(self):
        item, fetched = self.Next(1)
        if fetched:
            return item
        raise StopIteration

    def __getitem__(self, index):
        self.Reset()
        self.Skip(index)
        item, fetched = self.Next(1)
        if fetched:
            return item
        raise IndexError(index)

IEnumTfContextViews._methods_ = [
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IEnumTfContextViews)), 'ppenum' )),
    COMMETHOD([], HRESULT, 'Next',
              ( ['in'], c_ulong, 'ulCount' ),
              ( ['out'], POINTER(POINTER(ITfContextView)), 'rgViews' ),
              ( ['out'], POINTER(c_ulong), 'pcFetched' )),
    COMMETHOD([], HRESULT, 'Reset'),
    COMMETHOD([], HRESULT, 'Skip',
              ( ['in'], c_ulong, 'ulCount' )),
]
################################################################
## code template for IEnumTfContextViews implementation
##class IEnumTfContextViews_Impl(object):
##    def Reset(self):
##        '-no docstring-'
##        #return 
##
##    def Skip(self, ulCount):
##        '-no docstring-'
##        #return 
##
##    def Clone(self):
##        '-no docstring-'
##        #return ppenum
##
##    def Next(self, ulCount):
##        '-no docstring-'
##        #return rgViews, pcFetched
##

class TS_STATUS(Structure):
    _recordinfo_ = ('{C4E07FAB-27D8-45C1-A647-DB6D4F590C31}', 0, 0, 0L, '{FEC4F516-C503-45B1-A5FD-7A3D8AB07049}')
TF_STATUS = TS_STATUS
class IEnumTfContexts(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{8F1A7EA6-1654-4502-A86E-B2902344D507}')
    _idlflags_ = []
    def __iter__(self):
        return self

    def next(self):
        item, fetched = self.Next(1)
        if fetched:
            return item
        raise StopIteration

    def __getitem__(self, index):
        self.Reset()
        self.Skip(index)
        item, fetched = self.Next(1)
        if fetched:
            return item
        raise IndexError(index)

ITfDocumentMgr._methods_ = [
    COMMETHOD([], HRESULT, 'CreateContext',
              ( ['in'], TfClientId, 'tidOwner' ),
              ( ['in'], c_ulong, 'dwFlags' ),
              ( ['in'], POINTER(IUnknown), 'punk' ),
              ( ['out'], POINTER(POINTER(ITfContext)), 'ppic' ),
              ( ['out'], POINTER(TfEditCookie), 'pecTextStore' )),
    COMMETHOD([], HRESULT, 'Push',
              ( ['in'], POINTER(ITfContext), 'pic' )),
    COMMETHOD([], HRESULT, 'Pop',
              ( ['in'], c_ulong, 'dwFlags' )),
    COMMETHOD([], HRESULT, 'GetTop',
              ( ['out'], POINTER(POINTER(ITfContext)), 'ppic' )),
    COMMETHOD([], HRESULT, 'GetBase',
              ( ['out'], POINTER(POINTER(ITfContext)), 'ppic' )),
    COMMETHOD([], HRESULT, 'EnumContexts',
              ( ['out'], POINTER(POINTER(IEnumTfContexts)), 'ppenum' )),
]
################################################################
## code template for ITfDocumentMgr implementation
##class ITfDocumentMgr_Impl(object):
##    def CreateContext(self, tidOwner, dwFlags, punk):
##        '-no docstring-'
##        #return ppic, pecTextStore
##
##    def GetTop(self):
##        '-no docstring-'
##        #return ppic
##
##    def EnumContexts(self):
##        '-no docstring-'
##        #return ppenum
##
##    def Pop(self, dwFlags):
##        '-no docstring-'
##        #return 
##
##    def GetBase(self):
##        '-no docstring-'
##        #return ppic
##
##    def Push(self, pic):
##        '-no docstring-'
##        #return 
##

IBindCtx._methods_ = [
    COMMETHOD([], HRESULT, 'RegisterObjectBound',
              ( ['in'], POINTER(IUnknown), 'punk' )),
    COMMETHOD([], HRESULT, 'RevokeObjectBound',
              ( ['in'], POINTER(IUnknown), 'punk' )),
    COMMETHOD([], HRESULT, 'ReleaseBoundObjects'),
    COMMETHOD([], HRESULT, 'RemoteSetBindOptions',
              ( ['in'], POINTER(tagBIND_OPTS2), 'pbindopts' )),
    COMMETHOD([], HRESULT, 'RemoteGetBindOptions',
              ( ['in', 'out'], POINTER(tagBIND_OPTS2), 'pbindopts' )),
    COMMETHOD([], HRESULT, 'GetRunningObjectTable',
              ( ['out'], POINTER(POINTER(IRunningObjectTable)), 'pprot' )),
    COMMETHOD([], HRESULT, 'RegisterObjectParam',
              ( ['in'], WSTRING, 'pszKey' ),
              ( ['in'], POINTER(IUnknown), 'punk' )),
    COMMETHOD([], HRESULT, 'GetObjectParam',
              ( ['in'], WSTRING, 'pszKey' ),
              ( ['out'], POINTER(POINTER(IUnknown)), 'ppunk' )),
    COMMETHOD([], HRESULT, 'EnumObjectParam',
              ( ['out'], POINTER(POINTER(IEnumString)), 'ppenum' )),
    COMMETHOD([], HRESULT, 'RevokeObjectParam',
              ( ['in'], WSTRING, 'pszKey' )),
]
################################################################
## code template for IBindCtx implementation
##class IBindCtx_Impl(object):
##    def RemoteGetBindOptions(self):
##        '-no docstring-'
##        #return pbindopts
##
##    def RegisterObjectBound(self, punk):
##        '-no docstring-'
##        #return 
##
##    def RevokeObjectParam(self, pszKey):
##        '-no docstring-'
##        #return 
##
##    def ReleaseBoundObjects(self):
##        '-no docstring-'
##        #return 
##
##    def EnumObjectParam(self):
##        '-no docstring-'
##        #return ppenum
##
##    def GetObjectParam(self, pszKey):
##        '-no docstring-'
##        #return ppunk
##
##    def GetRunningObjectTable(self):
##        '-no docstring-'
##        #return pprot
##
##    def RevokeObjectBound(self, punk):
##        '-no docstring-'
##        #return 
##
##    def RemoteSetBindOptions(self, pbindopts):
##        '-no docstring-'
##        #return 
##
##    def RegisterObjectParam(self, pszKey, punk):
##        '-no docstring-'
##        #return 
##

class ITfCompartment(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{BB08F7A9-607A-4384-8623-056892B64371}')
    _idlflags_ = []
class IEnumGUID(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{0002E000-0000-0000-C000-000000000046}')
    _idlflags_ = []
ITfCompartmentMgr._methods_ = [
    COMMETHOD([], HRESULT, 'GetCompartment',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'rguid' ),
              ( ['out'], POINTER(POINTER(ITfCompartment)), 'ppcomp' )),
    COMMETHOD([], HRESULT, 'ClearCompartment',
              ( ['in'], TfClientId, 'tid' ),
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'rguid' )),
    COMMETHOD([], HRESULT, 'EnumCompartments',
              ( ['out'], POINTER(POINTER(IEnumGUID)), 'ppenum' )),
]
################################################################
## code template for ITfCompartmentMgr implementation
##class ITfCompartmentMgr_Impl(object):
##    def EnumCompartments(self):
##        '-no docstring-'
##        #return ppenum
##
##    def ClearCompartment(self, tid, rguid):
##        '-no docstring-'
##        #return 
##
##    def GetCompartment(self, rguid):
##        '-no docstring-'
##        #return ppcomp
##

TS_STATUS._fields_ = [
    ('dwDynamicFlags', c_ulong),
    ('dwStaticFlags', c_ulong),
]
assert sizeof(TS_STATUS) == 8, sizeof(TS_STATUS)
assert alignment(TS_STATUS) == 4, alignment(TS_STATUS)
class __MIDL_IWinTypes_0007(Union):
    pass
class _userBITMAP(Structure):
    pass
__MIDL_IWinTypes_0007._fields_ = [
    ('hInproc', c_int),
    ('hRemote', POINTER(_userBITMAP)),
    ('hInproc64', c_longlong),
]
assert sizeof(__MIDL_IWinTypes_0007) == 8, sizeof(__MIDL_IWinTypes_0007)
assert alignment(__MIDL_IWinTypes_0007) == 8, alignment(__MIDL_IWinTypes_0007)
_userHBITMAP._fields_ = [
    ('fContext', c_int),
    ('u', __MIDL_IWinTypes_0007),
]
assert sizeof(_userHBITMAP) == 16, sizeof(_userHBITMAP)
assert alignment(_userHBITMAP) == 8, alignment(_userHBITMAP)
IEnumTfRanges._methods_ = [
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IEnumTfRanges)), 'ppenum' )),
    COMMETHOD([], HRESULT, 'Next',
              ( ['in'], c_ulong, 'ulCount' ),
              ( ['out'], POINTER(POINTER(ITfRange)), 'ppRange' ),
              ( ['out'], POINTER(c_ulong), 'pcFetched' )),
    COMMETHOD([], HRESULT, 'Reset'),
    COMMETHOD([], HRESULT, 'Skip',
              ( [], c_ulong, 'ulCount' )),
]
################################################################
## code template for IEnumTfRanges implementation
##class IEnumTfRanges_Impl(object):
##    def Reset(self):
##        '-no docstring-'
##        #return 
##
##    def Skip(self, ulCount):
##        '-no docstring-'
##        #return 
##
##    def Clone(self):
##        '-no docstring-'
##        #return ppenum
##
##    def Next(self, ulCount):
##        '-no docstring-'
##        #return ppRange, pcFetched
##

IEnumSTATDATA._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteNext',
              ( ['in'], c_ulong, 'celt' ),
              ( ['out'], POINTER(tagSTATDATA), 'rgelt' ),
              ( ['out'], POINTER(c_ulong), 'pceltFetched' )),
    COMMETHOD([], HRESULT, 'Skip',
              ( ['in'], c_ulong, 'celt' )),
    COMMETHOD([], HRESULT, 'Reset'),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IEnumSTATDATA)), 'ppenum' )),
]
################################################################
## code template for IEnumSTATDATA implementation
##class IEnumSTATDATA_Impl(object):
##    def Reset(self):
##        '-no docstring-'
##        #return 
##
##    def Skip(self, celt):
##        '-no docstring-'
##        #return 
##
##    def Clone(self):
##        '-no docstring-'
##        #return ppenum
##
##    def RemoteNext(self, celt):
##        '-no docstring-'
##        #return rgelt, pceltFetched
##

class ITfEditSession(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{AA80E803-2021-11D2-93E0-0060B067B86E}')
    _idlflags_ = []
class ITfRangeBackup(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{463A506D-6992-49D2-9B88-93D55E70BB16}')
    _idlflags_ = []
ITfContext._methods_ = [
    COMMETHOD([], HRESULT, 'RequestEditSession',
              ( ['in'], TfClientId, 'tid' ),
              ( ['in'], POINTER(ITfEditSession), 'pes' ),
              ( ['in'], c_ulong, 'dwFlags' ),
              ( ['out'], POINTER(HRESULT), 'phrSession' )),
    COMMETHOD([], HRESULT, 'InWriteSession',
              ( ['in'], TfClientId, 'tid' ),
              ( ['out'], POINTER(c_int), 'pfWriteSession' )),
    COMMETHOD([], HRESULT, 'GetSelection',
              ( ['in'], TfEditCookie, 'ec' ),
              ( ['in'], c_ulong, 'ulIndex' ),
              ( ['in'], c_ulong, 'ulCount' ),
              ( ['out'], POINTER(TF_SELECTION), 'pSelection' ),
              ( ['out'], POINTER(c_ulong), 'pcFetched' )),
    COMMETHOD([], HRESULT, 'SetSelection',
              ( ['in'], TfEditCookie, 'ec' ),
              ( ['in'], c_ulong, 'ulCount' ),
              ( ['in'], POINTER(TF_SELECTION), 'pSelection' )),
    COMMETHOD([], HRESULT, 'GetStart',
              ( ['in'], TfEditCookie, 'ec' ),
              ( ['out'], POINTER(POINTER(ITfRange)), 'ppStart' )),
    COMMETHOD([], HRESULT, 'GetEnd',
              ( ['in'], TfEditCookie, 'ec' ),
              ( ['out'], POINTER(POINTER(ITfRange)), 'ppEnd' )),
    COMMETHOD([], HRESULT, 'GetActiveView',
              ( ['out'], POINTER(POINTER(ITfContextView)), 'ppView' )),
    COMMETHOD([], HRESULT, 'EnumViews',
              ( ['out'], POINTER(POINTER(IEnumTfContextViews)), 'ppenum' )),
    COMMETHOD([], HRESULT, 'GetStatus',
              ( ['out'], POINTER(TF_STATUS), 'pdcs' )),
    COMMETHOD([], HRESULT, 'GetProperty',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'guidProp' ),
              ( ['out'], POINTER(POINTER(ITfProperty)), 'ppProp' )),
    COMMETHOD([], HRESULT, 'GetAppProperty',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'guidProp' ),
              ( ['out'], POINTER(POINTER(ITfReadOnlyProperty)), 'ppProp' )),
    COMMETHOD([], HRESULT, 'TrackProperties',
              ( ['in'], POINTER(POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID)), 'prgProp' ),
              ( ['in'], c_ulong, 'cProp' ),
              ( ['in'], POINTER(POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID)), 'prgAppProp' ),
              ( ['in'], c_ulong, 'cAppProp' ),
              ( ['out'], POINTER(POINTER(ITfReadOnlyProperty)), 'ppProperty' )),
    COMMETHOD([], HRESULT, 'EnumProperties',
              ( ['out'], POINTER(POINTER(IEnumTfProperties)), 'ppenum' )),
    COMMETHOD([], HRESULT, 'GetDocumentMgr',
              ( ['out'], POINTER(POINTER(ITfDocumentMgr)), 'ppDm' )),
    COMMETHOD([], HRESULT, 'CreateRangeBackup',
              ( ['in'], TfEditCookie, 'ec' ),
              ( ['in'], POINTER(ITfRange), 'pRange' ),
              ( ['out'], POINTER(POINTER(ITfRangeBackup)), 'ppBackup' )),
]
################################################################
## code template for ITfContext implementation
##class ITfContext_Impl(object):
##    def EnumProperties(self):
##        '-no docstring-'
##        #return ppenum
##
##    def EnumViews(self):
##        '-no docstring-'
##        #return ppenum
##
##    def TrackProperties(self, prgProp, cProp, prgAppProp, cAppProp):
##        '-no docstring-'
##        #return ppProperty
##
##    def SetSelection(self, ec, ulCount, pSelection):
##        '-no docstring-'
##        #return 
##
##    def GetStart(self, ec):
##        '-no docstring-'
##        #return ppStart
##
##    def GetAppProperty(self, guidProp):
##        '-no docstring-'
##        #return ppProp
##
##    def GetSelection(self, ec, ulIndex, ulCount):
##        '-no docstring-'
##        #return pSelection, pcFetched
##
##    def GetStatus(self):
##        '-no docstring-'
##        #return pdcs
##
##    def CreateRangeBackup(self, ec, pRange):
##        '-no docstring-'
##        #return ppBackup
##
##    def GetActiveView(self):
##        '-no docstring-'
##        #return ppView
##
##    def GetDocumentMgr(self):
##        '-no docstring-'
##        #return ppDm
##
##    def GetProperty(self, guidProp):
##        '-no docstring-'
##        #return ppProp
##
##    def InWriteSession(self, tid):
##        '-no docstring-'
##        #return pfWriteSession
##
##    def GetEnd(self, ec):
##        '-no docstring-'
##        #return ppEnd
##
##    def RequestEditSession(self, tid, pes, dwFlags):
##        '-no docstring-'
##        #return phrSession
##

ITfCompartment._methods_ = [
    COMMETHOD([], HRESULT, 'SetValue',
              ( ['in'], TfClientId, 'tid' ),
              ( ['in'], POINTER(VARIANT), 'pvarValue' )),
    COMMETHOD([], HRESULT, 'GetValue',
              ( ['out'], POINTER(VARIANT), 'pvarValue' )),
]
################################################################
## code template for ITfCompartment implementation
##class ITfCompartment_Impl(object):
##    def SetValue(self, tid, pvarValue):
##        '-no docstring-'
##        #return 
##
##    def GetValue(self):
##        '-no docstring-'
##        #return pvarValue
##

ITfRangeBackup._methods_ = [
    COMMETHOD([], HRESULT, 'Restore',
              ( ['in'], TfEditCookie, 'ec' ),
              ( ['in'], POINTER(ITfRange), 'pRange' )),
]
################################################################
## code template for ITfRangeBackup implementation
##class ITfRangeBackup_Impl(object):
##    def Restore(self, ec, pRange):
##        '-no docstring-'
##        #return 
##

IEnumGUID._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteNext',
              ( ['in'], c_ulong, 'celt' ),
              ( ['out'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'rgelt' ),
              ( ['out'], POINTER(c_ulong), 'pceltFetched' )),
    COMMETHOD([], HRESULT, 'Skip',
              ( ['in'], c_ulong, 'celt' )),
    COMMETHOD([], HRESULT, 'Reset'),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IEnumGUID)), 'ppenum' )),
]
################################################################
## code template for IEnumGUID implementation
##class IEnumGUID_Impl(object):
##    def Reset(self):
##        '-no docstring-'
##        #return 
##
##    def Skip(self, celt):
##        '-no docstring-'
##        #return 
##
##    def Clone(self):
##        '-no docstring-'
##        #return ppenum
##
##    def RemoteNext(self, celt):
##        '-no docstring-'
##        #return rgelt, pceltFetched
##

_userHGLOBAL._fields_ = [
    ('fContext', c_int),
    ('u', __MIDL_IWinTypes_0003),
]
assert sizeof(_userHGLOBAL) == 16, sizeof(_userHGLOBAL)
assert alignment(_userHGLOBAL) == 8, alignment(_userHGLOBAL)
_userBITMAP._fields_ = [
    ('bmType', c_int),
    ('bmWidth', c_int),
    ('bmHeight', c_int),
    ('bmWidthBytes', c_int),
    ('bmPlanes', c_ushort),
    ('bmBitsPixel', c_ushort),
    ('cbSize', c_ulong),
    ('pBuffer', POINTER(c_ubyte)),
]
assert sizeof(_userBITMAP) == 28, sizeof(_userBITMAP)
assert alignment(_userBITMAP) == 4, alignment(_userBITMAP)
class __MIDL_IWinTypes_0008(Union):
    pass
__MIDL_IWinTypes_0008._fields_ = [
    ('hInproc', c_int),
    ('hRemote', POINTER(tagLOGPALETTE)),
    ('hInproc64', c_longlong),
]
assert sizeof(__MIDL_IWinTypes_0008) == 8, sizeof(__MIDL_IWinTypes_0008)
assert alignment(__MIDL_IWinTypes_0008) == 8, alignment(__MIDL_IWinTypes_0008)
_userHPALETTE._fields_ = [
    ('fContext', c_int),
    ('u', __MIDL_IWinTypes_0008),
]
assert sizeof(_userHPALETTE) == 16, sizeof(_userHPALETTE)
assert alignment(_userHPALETTE) == 8, alignment(_userHPALETTE)
ITfEditSession._methods_ = [
    COMMETHOD([], HRESULT, 'DoEditSession',
              ( ['in'], TfEditCookie, 'ec' )),
]
################################################################
## code template for ITfEditSession implementation
##class ITfEditSession_Impl(object):
##    def DoEditSession(self, ec):
##        '-no docstring-'
##        #return 
##

IEnumTfContexts._methods_ = [
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IEnumTfContexts)), 'ppenum' )),
    COMMETHOD([], HRESULT, 'Next',
              ( ['in'], c_ulong, 'ulCount' ),
              ( ['out'], POINTER(POINTER(ITfContext)), 'rgContext' ),
              ( ['out'], POINTER(c_ulong), 'pcFetched' )),
    COMMETHOD([], HRESULT, 'Reset'),
    COMMETHOD([], HRESULT, 'Skip',
              ( ['in'], c_ulong, 'ulCount' )),
]
################################################################
## code template for IEnumTfContexts implementation
##class IEnumTfContexts_Impl(object):
##    def Reset(self):
##        '-no docstring-'
##        #return 
##
##    def Skip(self, ulCount):
##        '-no docstring-'
##        #return 
##
##    def Clone(self):
##        '-no docstring-'
##        #return ppenum
##
##    def Next(self, ulCount):
##        '-no docstring-'
##        #return rgContext, pcFetched
##

IEnumTfDocumentMgrs._methods_ = [
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IEnumTfDocumentMgrs)), 'ppenum' )),
    COMMETHOD([], HRESULT, 'Next',
              ( ['in'], c_ulong, 'ulCount' ),
              ( ['out'], POINTER(POINTER(ITfDocumentMgr)), 'rgDocumentMgr' ),
              ( ['out'], POINTER(c_ulong), 'pcFetched' )),
    COMMETHOD([], HRESULT, 'Reset'),
    COMMETHOD([], HRESULT, 'Skip',
              ( ['in'], c_ulong, 'ulCount' )),
]
################################################################
## code template for IEnumTfDocumentMgrs implementation
##class IEnumTfDocumentMgrs_Impl(object):
##    def Reset(self):
##        '-no docstring-'
##        #return 
##
##    def Skip(self, ulCount):
##        '-no docstring-'
##        #return 
##
##    def Clone(self):
##        '-no docstring-'
##        #return ppenum
##
##    def Next(self, ulCount):
##        '-no docstring-'
##        #return rgDocumentMgr, pcFetched
##

__all__ = ['_userFLAG_STGMEDIUM', 'IEnumGUID', 'wireCLIPFORMAT',
           'ITfEditSession', 'tagSTATSTG', '_userBITMAP',
           'ITfFunctionProvider', 'IEnumTfContextViews',
           'TF_HALTCOND', '_RemotableHandle', 'IEnumString',
           'IPersistStream', '__MIDL_IWinTypes_0001',
           '__MIDL_IWinTypes_0003', '_userHBITMAP',
           '__MIDL_IWinTypes_0005', '__MIDL_IWinTypes_0004',
           '__MIDL_IWinTypes_0007', '__MIDL_IWinTypes_0006',
           '__MIDL_IWinTypes_0009', '__MIDL_IWinTypes_0008',
           '_userCLIPFORMAT', '_STGMEDIUM_UNION', 'ITfDocumentMgr',
           '__MIDL_ITfContext_0001', 'IMoniker', 'TF_STATUS',
           'TfAnchor', 'IEnumTfContexts', 'IStream', '_userHGLOBAL',
           'ITfContextView', '_userHPALETTE', 'wireASYNC_STGMEDIUM',
           'TfEditCookie', 'tagSTATDATA', 'TF_GRAVITY_FORWARD',
           'TfShiftDir', '_BYTE_BLOB', 'TF_AE_START',
           '_userHENHMETAFILE', 'ITfRangeBackup', 'TS_STATUS',
           'tagDVTARGETDEVICE', 'TF_ANCHOR_START',
           'ISequentialStream', 'wireSTGMEDIUM', 'ITfRange',
           'TF_SD_BACKWARD', 'IEnumTfRanges', 'ITfContext',
           'IBindCtx', '_userHMETAFILEPICT', 'ITfThreadMgr',
           'TfGravity', 'tagLOGPALETTE',
           '__MIDL___MIDL_itf_bogo_0001_0064_0001', 'ITfProperty',
           '__MIDL_IAdviseSink_0003', '__MIDL_IAdviseSink_0002',
           'wireFLAG_STGMEDIUM', 'IEnumTfProperties', 'TF_SELECTION',
           'TF_AE_NONE', '_GDI_OBJECT', '_userHMETAFILE',
           'TF_SELECTIONSTYLE', 'IEnumTfFunctionProviders',
           'ITfPropertyStore', 'ITfCompartment', 'IEnumFORMATETC',
           '_FLAGGED_BYTE_BLOB', 'IEnumSTATDATA', 'IDataObject',
           'TF_GRAVITY_BACKWARD', 'ITfReadOnlyProperty', 'BoGo',
           'TF_ANCHOR_END', 'TF_AE_END', 'tagFORMATETC',
           '_remoteMETAFILEPICT', 'tagPALETTEENTRY', 'TfActiveSelEnd',
           'IRunningObjectTable', '__MIDL_ITfRange_0001',
           '__MIDL_ITfRange_0002', '_userSTGMEDIUM',
           'ITfTextInputProcessor', 'IEnumMoniker',
           'ITfCompartmentMgr', 'IAdviseSink', 'TF_SD_FORWARD',
           'TfClientId', 'IEnumTfDocumentMgrs']
from comtypes import _check_version; _check_version('501')
