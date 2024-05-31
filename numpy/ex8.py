#joining two arrays
#we can use concatenate to join two arrays
import  numpy as n
x=n.array([10,20,30])
y=n.array([40,50,60])

print(x+y)
z=n.concatenate((x,y))
print(z)

#split:
z=n.array([10,20,30,40,50,60])
a=n.split(z,2)
print(a)

