Python 3.2.2 (default, Sep  4 2011, 09:51:08) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def reverse3(nums):
	#return [nums[2], nums[1], nums[0]]
	 return nums[::-1]

	
>>> reverse3([1, 2, 3])
[3, 2, 1]
>>> reverse3([5, 11, 9])
[9, 11, 5]
>>> reverse3([7, 0, 0])
[0, 0, 7]
>>> 
