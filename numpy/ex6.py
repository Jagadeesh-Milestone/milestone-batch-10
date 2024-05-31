#shape of an array
#it is the number of elements in each dimension
import  numpy as n
x=n.array([10,20,30,40])
print(x)
print(x.shape)
y=n.array([[10,20,30,50],[40,50,60,80]])
print(y.shape)
z=n.array([1,2,3,4,5],ndmin=7)
print(z.shape)
#reshape:
a=n.array([1,2,3,4,5,6,7,8,9,10])
print(a.shape)
b=a.reshape(2,5)
print(b)
c=a.reshape(5,2)
print(c)