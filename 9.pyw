Python 3.2.2 (default, Sep  4 2011, 09:51:08) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = int(input("Input integer : "))
Input integer : 5
>>> n1 = int( "%s" % a )
>>> n2 = int( "%s%s" % (a,a) )
>>> n3 = int( "%s%s%s" % (a,a,a) )
>>> print (n1+n2+n3)
615
>>> 
