Python 3.2.2 (default, Sep  4 2011, 09:51:08) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from datetime import date
>>> f_date = date(2017, 12, 13)
>>> l_date = date(2017, 12, 11)
>>> 
KeyboardInterrupt
>>> delta = l_date - f_date
>>> print(delta.days)
-2
>>> 
