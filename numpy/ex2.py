#creating an array:
import numpy as n
x=n.array([10,20,30,40,50])
print(x)
print(type(x))

#dimensions
#it is the deapth of an array
#zero dimensional array:
a=n.array(10)
print(a)
print(a.ndim)
print(type(a))

#one dimensional array:
b=n.array([10,20,30,40])
print(b)
print(b.ndim)
print(type(b))

#two dimensional array
c=n.array([[10,20,30],[40,50,60]])
print(c)
print(c.ndim)

#three dimensional array:
d=n.array([[[1,2],[3,4]],[[5,6],[7,8]],[[9,10],[11,12]]])
print(d)
print(d.ndim)

#multi dimensional array:
e=n.array([10,20,30,40,50],ndmin=7)
print(e)
print(e.ndim)