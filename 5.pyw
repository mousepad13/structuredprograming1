Python 3.2.2 (default, Sep  4 2011, 09:51:08) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> values = input("Input some comma seprated numbers : ")
Input some comma seprated numbers : 3,4,6,9
>>> list = values.split(",")
>>> tuple = tuple(list)
>>> print('List : ',list)
List :  ['3', '4', '6', '9']
>>> print('Tuple : ',tuple)
Tuple :  ('3', '4', '6', '9')
>>> 
