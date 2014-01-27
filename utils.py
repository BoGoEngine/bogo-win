import ctypes


def text_to_ushort_array(text):
    return ctypes.cast(ctypes.c_wchar_p(text), ctypes.POINTER(ctypes.c_ushort))


def ushort_array_to_unicode(ushort_array, length):
    # FIXME: Very inefficient. Should investigate automatic conversion
    # using open() and in-memory buffer.
    string = u''
    for i in xrange(length):
        c = unichr(ushort_array[i])
        string += c
    return string


if __name__ == '__main__':
	ushort_array = text_to_ushort_array("bogo")
	expected = "bogo"
	assert ushort_array_to_unicode(ushort_array, 4) == expected
