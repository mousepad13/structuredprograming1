Python 3.2.2 (default, Sep  4 2011, 09:51:08) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def common_end(a, b):
	return a[0] == b[0] or a[-1] == b[-1]

>>> common_end([1, 2, 3], [7, 3])
True
>>> common_end([1, 2, 3], [7, 3, 2])
False
>>> common_end([1, 2, 3], [1, 3])
True
>>> 
