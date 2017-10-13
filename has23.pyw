Python 3.2.2 (default, Sep  4 2011, 09:51:08) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def has23(nums):
	return 2 in nums or 3 in nums

>>> has23([2, 5])
True
>>> has23([4, 3])
True
>>> has23([4, 5])
False
>>> 
