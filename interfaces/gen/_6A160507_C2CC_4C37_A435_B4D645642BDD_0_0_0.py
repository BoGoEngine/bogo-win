# -*- coding: mbcs -*-
typelib_path = 'd:\\bogo\\bogo-win32\\interfaces\\tsf.tlb'
_lcid = 0 # change this if required
from ctypes import *
from comtypes import GUID
from comtypes import IUnknown
from comtypes import GUID
from ctypes import HRESULT
from comtypes import BSTR
TfGuidAtom = c_ulong
from comtypes import helpstring
from comtypes import COMMETHOD
from comtypes import dispid
UINT_PTR = c_ulong
from ctypes.wintypes import HKL
from comtypes import CoClass


class ITfCategoryMgr(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{C3ACEFB5-F69D-4905-938F-FCADCF4BE830}')
    _idlflags_ = []
class IEnumGUID(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{0002E000-0000-0000-C000-000000000046}')
    _idlflags_ = []
ITfCategoryMgr._methods_ = [
    COMMETHOD([], HRESULT, 'RegisterCategory',
              ( ['in'], POINTER(GUID), 'rclsid' ),
              ( ['in'], POINTER(GUID), 'rcatid' ),
              ( ['in'], POINTER(GUID), 'rguid' )),
    COMMETHOD([], HRESULT, 'UnregisterCategory',
              ( ['in'], POINTER(GUID), 'rclsid' ),
              ( ['in'], POINTER(GUID), 'rcatid' ),
              ( ['in'], POINTER(GUID), 'rguid' )),
    COMMETHOD([], HRESULT, 'EnumCategoriesInItem',
              ( ['in'], POINTER(GUID), 'rguid' ),
              ( ['out'], POINTER(POINTER(IEnumGUID)), 'ppenum' )),
    COMMETHOD([], HRESULT, 'EnumItemsInCategory',
              ( ['in'], POINTER(GUID), 'rcatid' ),
              ( ['out'], POINTER(POINTER(IEnumGUID)), 'ppenum' )),
    COMMETHOD([], HRESULT, 'FindClosestCategory',
              ( ['in'], POINTER(GUID), 'rguid' ),
              ( ['out'], POINTER(GUID), 'pcatid' ),
              ( ['in'], POINTER(POINTER(GUID)), 'ppcatidList' ),
              ( ['in'], c_ulong, 'ulCount' )),
    COMMETHOD([], HRESULT, 'RegisterGUIDDescription',
              ( ['in'], POINTER(GUID), 'rclsid' ),
              ( ['in'], POINTER(GUID), 'rguid' ),
              ( ['in'], POINTER(c_ushort), 'pchDesc' ),
              ( ['in'], c_ulong, 'cch' )),
    COMMETHOD([], HRESULT, 'UnregisterGUIDDescription',
              ( ['in'], POINTER(GUID), 'rclsid' ),
              ( ['in'], POINTER(GUID), 'rguid' )),
    COMMETHOD([], HRESULT, 'GetGUIDDescription',
              ( ['in'], POINTER(GUID), 'rguid' ),
              ( ['out'], POINTER(BSTR), 'pbstrDesc' )),
    COMMETHOD([], HRESULT, 'RegisterGUIDDWORD',
              ( ['in'], POINTER(GUID), 'rclsid' ),
              ( ['in'], POINTER(GUID), 'rguid' ),
              ( ['in'], c_ulong, 'dw' )),
    COMMETHOD([], HRESULT, 'UnregisterGUIDDWORD',
              ( ['in'], POINTER(GUID), 'rclsid' ),
              ( ['in'], POINTER(GUID), 'rguid' )),
    COMMETHOD([], HRESULT, 'GetGUIDDWORD',
              ( ['in'], POINTER(GUID), 'rguid' ),
              ( ['out'], POINTER(c_ulong), 'pdw' )),
    COMMETHOD([], HRESULT, 'RegisterGUID',
              ( ['in'], POINTER(GUID), 'rguid' ),
              ( ['out'], POINTER(TfGuidAtom), 'pguidatom' )),
    COMMETHOD([], HRESULT, 'GetGUID',
              ( ['in'], TfGuidAtom, 'guidatom' ),
              ( ['out'], POINTER(GUID), 'pguid' )),
    COMMETHOD([], HRESULT, 'IsEqualTfGuidAtom',
              ( ['in'], TfGuidAtom, 'guidatom' ),
              ( ['in'], POINTER(GUID), 'rguid' ),
              ( ['out'], POINTER(c_int), 'pfEqual' )),
]
################################################################
## code template for ITfCategoryMgr implementation
##class ITfCategoryMgr_Impl(object):
##    def RegisterGUIDDescription(self, rclsid, rguid, pchDesc, cch):
##        '-no docstring-'
##        #return 
##
##    def IsEqualTfGuidAtom(self, guidatom, rguid):
##        '-no docstring-'
##        #return pfEqual
##
##    def GetGUIDDescription(self, rguid):
##        '-no docstring-'
##        #return pbstrDesc
##
##    def RegisterCategory(self, rclsid, rcatid, rguid):
##        '-no docstring-'
##        #return 
##
##    def UnregisterGUIDDescription(self, rclsid, rguid):
##        '-no docstring-'
##        #return 
##
##    def FindClosestCategory(self, rguid, ppcatidList, ulCount):
##        '-no docstring-'
##        #return pcatid
##
##    def GetGUIDDWORD(self, rguid):
##        '-no docstring-'
##        #return pdw
##
##    def UnregisterGUIDDWORD(self, rclsid, rguid):
##        '-no docstring-'
##        #return 
##
##    def RegisterGUIDDWORD(self, rclsid, rguid, dw):
##        '-no docstring-'
##        #return 
##
##    def RegisterGUID(self, rguid):
##        '-no docstring-'
##        #return pguidatom
##
##    def UnregisterCategory(self, rclsid, rcatid, rguid):
##        '-no docstring-'
##        #return 
##
##    def EnumCategoriesInItem(self, rguid):
##        '-no docstring-'
##        #return ppenum
##
##    def GetGUID(self, guidatom):
##        '-no docstring-'
##        #return pguid
##
##    def EnumItemsInCategory(self, rcatid):
##        '-no docstring-'
##        #return ppenum
##

class IEnumTfLanguageProfiles(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{3D61BF11-AC5F-42C8-A4CB-931BCC28C744}')
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

class TF_LANGUAGEPROFILE(Structure):
    _recordinfo_ = ('{6A160507-C2CC-4C37-A435-B4D645642BDD}', 0, 0, 0L, '{E1B5808D-1E46-4C19-84DC-68C5F5978CC8}')
IEnumTfLanguageProfiles._methods_ = [
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IEnumTfLanguageProfiles)), 'ppenum' )),
    COMMETHOD([], HRESULT, 'Next',
              ( ['in'], c_ulong, 'ulCount' ),
              ( ['out'], POINTER(TF_LANGUAGEPROFILE), 'pProfile' ),
              ( ['out'], POINTER(c_ulong), 'pcFetch' )),
    COMMETHOD([], HRESULT, 'Reset'),
    COMMETHOD([], HRESULT, 'Skip',
              ( ['in'], c_ulong, 'ulCount' )),
]
################################################################
## code template for IEnumTfLanguageProfiles implementation
##class IEnumTfLanguageProfiles_Impl(object):
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
##        #return pProfile, pcFetch
##

IEnumGUID._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteNext',
              ( ['in'], c_ulong, 'celt' ),
              ( ['out'], POINTER(GUID), 'rgelt' ),
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

class __MIDL___MIDL_itf_tsf_0006_0001_0001(Structure):
    pass
__MIDL___MIDL_itf_tsf_0006_0001_0001._fields_ = [
    ('Data1', c_ulong),
    ('Data2', c_ushort),
    ('Data3', c_ushort),
    ('Data4', c_ubyte * 8),
]
assert sizeof(__MIDL___MIDL_itf_tsf_0006_0001_0001) == 16, sizeof(__MIDL___MIDL_itf_tsf_0006_0001_0001)
assert alignment(__MIDL___MIDL_itf_tsf_0006_0001_0001) == 4, alignment(__MIDL___MIDL_itf_tsf_0006_0001_0001)
TF_LANGUAGEPROFILE._fields_ = [
    ('clsid', GUID),
    ('langid', c_ushort),
    ('catid', GUID),
    ('fActive', c_int),
    ('guidProfile', GUID),
]
assert sizeof(TF_LANGUAGEPROFILE) == 56, sizeof(TF_LANGUAGEPROFILE)
assert alignment(TF_LANGUAGEPROFILE) == 4, alignment(TF_LANGUAGEPROFILE)
class Library(object):
    name = u'TSF'
    _reg_typelib_ = ('{6A160507-C2CC-4C37-A435-B4D645642BDD}', 0, 0)

class ITfInputProcessorProfiles(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{1F02B6C5-7842-4EE6-8A0B-9A24183A95CA}')
    _idlflags_ = []
ITfInputProcessorProfiles._methods_ = [
    COMMETHOD([], HRESULT, 'Register',
              ( ['in'], POINTER(GUID), 'rclsid' )),
    COMMETHOD([], HRESULT, 'Unregister',
              ( ['in'], POINTER(GUID), 'rclsid' )),
    COMMETHOD([], HRESULT, 'AddLanguageProfile',
              ( ['in'], POINTER(GUID), 'rclsid' ),
              ( ['in'], c_ushort, 'langid' ),
              ( ['in'], POINTER(GUID), 'guidProfile' ),
              ( ['in'], POINTER(c_ushort), 'pchDesc' ),
              ( ['in'], c_ulong, 'cchDesc' ),
              ( ['in'], POINTER(c_ushort), 'pchIconFile' ),
              ( ['in'], c_ulong, 'cchFile' ),
              ( ['in'], c_ulong, 'uIconIndex' )),
    COMMETHOD([], HRESULT, 'RemoveLanguageProfile',
              ( ['in'], POINTER(GUID), 'rclsid' ),
              ( ['in'], c_ushort, 'langid' ),
              ( ['in'], POINTER(GUID), 'guidProfile' )),
    COMMETHOD([], HRESULT, 'EnumInputProcessorInfo',
              ( ['out'], POINTER(POINTER(IEnumGUID)), 'ppenum' )),
    COMMETHOD([], HRESULT, 'GetDefaultLanguageProfile',
              ( ['in'], c_ushort, 'langid' ),
              ( ['in'], POINTER(GUID), 'catid' ),
              ( ['out'], POINTER(GUID), 'pclsid' ),
              ( ['out'], POINTER(GUID), 'pguidProfile' )),
    COMMETHOD([], HRESULT, 'SetDefaultLanguageProfile',
              ( ['in'], c_ushort, 'langid' ),
              ( ['in'], POINTER(GUID), 'rclsid' ),
              ( ['in'], POINTER(GUID), 'guidProfiles' )),
    COMMETHOD([], HRESULT, 'ActivateLanguageProfile',
              ( ['in'], POINTER(GUID), 'rclsid' ),
              ( ['in'], c_ushort, 'langid' ),
              ( ['in'], POINTER(GUID), 'guidProfiles' )),
    COMMETHOD([], HRESULT, 'GetActiveLanguageProfile',
              ( ['in'], POINTER(GUID), 'rclsid' ),
              ( ['out'], POINTER(c_ushort), 'plangid' ),
              ( ['out'], POINTER(GUID), 'pguidProfile' )),
    COMMETHOD([], HRESULT, 'GetLanguageProfileDescription',
              ( ['in'], POINTER(GUID), 'rclsid' ),
              ( ['in'], c_ushort, 'langid' ),
              ( ['in'], POINTER(GUID), 'guidProfile' ),
              ( ['out'], POINTER(BSTR), 'pbstrProfile' )),
    COMMETHOD([], HRESULT, 'GetCurrentLanguage',
              ( ['out'], POINTER(c_ushort), 'plangid' )),
    COMMETHOD([], HRESULT, 'ChangeCurrentLanguage',
              ( ['in'], c_ushort, 'langid' )),
    COMMETHOD([], HRESULT, 'GetLanguageList',
              ( ['out'], POINTER(POINTER(c_ushort)), 'ppLangId' ),
              ( ['out'], POINTER(c_ulong), 'pulCount' )),
    COMMETHOD([], HRESULT, 'EnumLanguageProfiles',
              ( ['in'], c_ushort, 'langid' ),
              ( ['out'], POINTER(POINTER(IEnumTfLanguageProfiles)), 'ppenum' )),
    COMMETHOD([], HRESULT, 'EnableLanguageProfile',
              ( ['in'], POINTER(GUID), 'rclsid' ),
              ( ['in'], c_ushort, 'langid' ),
              ( ['in'], POINTER(GUID), 'guidProfile' ),
              ( ['in'], c_int, 'fEnable' )),
    COMMETHOD([], HRESULT, 'IsEnabledLanguageProfile',
              ( ['in'], POINTER(GUID), 'rclsid' ),
              ( ['in'], c_ushort, 'langid' ),
              ( ['in'], POINTER(GUID), 'guidProfile' ),
              ( ['out'], POINTER(c_int), 'pfEnable' )),
    COMMETHOD([], HRESULT, 'EnableLanguageProfileByDefault',
              ( ['in'], POINTER(GUID), 'rclsid' ),
              ( ['in'], c_ushort, 'langid' ),
              ( ['in'], POINTER(GUID), 'guidProfile' ),
              ( ['in'], c_int, 'fEnable' )),
    COMMETHOD([], HRESULT, 'SubstituteKeyboardLayout',
              ( ['in'], POINTER(GUID), 'rclsid' ),
              ( ['in'], c_ushort, 'langid' ),
              ( ['in'], POINTER(GUID), 'guidProfile' ),
              ( ['in'], HKL, 'HKL' )),
]
################################################################
## code template for ITfInputProcessorProfiles implementation
##class ITfInputProcessorProfiles_Impl(object):
##    def EnumInputProcessorInfo(self):
##        '-no docstring-'
##        #return ppenum
##
##    def EnumLanguageProfiles(self, langid):
##        '-no docstring-'
##        #return ppenum
##
##    def GetDefaultLanguageProfile(self, langid, catid):
##        '-no docstring-'
##        #return pclsid, pguidProfile
##
##    def Unregister(self, rclsid):
##        '-no docstring-'
##        #return 
##
##    def GetLanguageList(self):
##        '-no docstring-'
##        #return ppLangId, pulCount
##
##    def GetCurrentLanguage(self):
##        '-no docstring-'
##        #return plangid
##
##    def Register(self, rclsid):
##        '-no docstring-'
##        #return 
##
##    def ActivateLanguageProfile(self, rclsid, langid, guidProfiles):
##        '-no docstring-'
##        #return 
##
##    def RemoveLanguageProfile(self, rclsid, langid, guidProfile):
##        '-no docstring-'
##        #return 
##
##    def AddLanguageProfile(self, rclsid, langid, guidProfile, pchDesc, cchDesc, pchIconFile, cchFile, uIconIndex):
##        '-no docstring-'
##        #return 
##
##    def EnableLanguageProfile(self, rclsid, langid, guidProfile, fEnable):
##        '-no docstring-'
##        #return 
##
##    def ChangeCurrentLanguage(self, langid):
##        '-no docstring-'
##        #return 
##
##    def SubstituteKeyboardLayout(self, rclsid, langid, guidProfile, HKL):
##        '-no docstring-'
##        #return 
##
##    def IsEnabledLanguageProfile(self, rclsid, langid, guidProfile):
##        '-no docstring-'
##        #return pfEnable
##
##    def GetLanguageProfileDescription(self, rclsid, langid, guidProfile):
##        '-no docstring-'
##        #return pbstrProfile
##
##    def GetActiveLanguageProfile(self, rclsid):
##        '-no docstring-'
##        #return plangid, pguidProfile
##
##    def SetDefaultLanguageProfile(self, langid, rclsid, guidProfiles):
##        '-no docstring-'
##        #return 
##
##    def EnableLanguageProfileByDefault(self, rclsid, langid, guidProfile, fEnable):
##        '-no docstring-'
##        #return 
##

class FakeClass(CoClass):
    _reg_clsid_ = GUID('{DEC2C382-120C-4D57-BEDA-9C15678C863F}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{6A160507-C2CC-4C37-A435-B4D645642BDD}', 0, 0)
FakeClass._com_interfaces_ = [ITfInputProcessorProfiles, ITfCategoryMgr]

__all__ = ['ITfInputProcessorProfiles', 'TF_LANGUAGEPROFILE',
           'IEnumTfLanguageProfiles', 'TfGuidAtom', 'FakeClass',
           'UINT_PTR', 'IEnumGUID', 'ITfCategoryMgr',
           '__MIDL___MIDL_itf_tsf_0006_0001_0001']
from comtypes import _check_version; _check_version('501')
