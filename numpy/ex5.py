#copy and view
import  numpy as n
x=n.array([10,20,30,40])
y=x.copy()
x[0]=100
print(x)
print(y)
#the copied array values will not be changed along with original array
a=n.array([1,2,3,4,5])
b=a.view()
a[0]=10
print(a)
print(b)
#the viewed valued will be changed along with original array

#check for original array
s=n.array([10,20,30,40,50])
t=s.copy()
v=s.view()

print(t.base)
print(v.base)