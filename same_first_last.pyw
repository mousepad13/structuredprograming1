Python 3.2.2 (default, Sep  4 2011, 09:51:08) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def same_first_last(nums):
	return len(nums) >= 1 and nums[0] == nums[-1]

>>> 
same_first_last([1, 2, 3])
False
>>> same_first_last([1, 2, 3, 1])
True
>>> same_first_last([1, 2, 1])
True
>>> 
