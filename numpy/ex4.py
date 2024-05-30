#data types in array:
import  numpy as n

x=n.array([1,2,3,4,5])
print(x)
print(x.dtype)

y=n.array([10.2,10.4,5.7])
print(y)
print(y.dtype)

z=n.array(['python','java','html','javascript','ruby','jagadeesh kumar'])
print(z)
print(z.dtype)

#change the data type(type casting)
a=n.array([1,0,3,6,0])
b=a.astype(bool)
print(b)
print(b.dtype)

c=n.array([10.3,11.4,12.7])
d=c.astype('i')
e=c.astype(int)
print(d)
print(e)
print(d.dtype)
print(e.dtype)