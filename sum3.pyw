Python 3.2.2 (default, Sep  4 2011, 09:51:08) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def sum3(nums):
	 #return nums[0] + nums[1] + nums[2]
	 return sum(nums)

	
>>> sum3([1, 2, 3])
6
>>> sum3([5, 11, 2])
18
>>> sum3([7, 0, 0])
7
>>> 
