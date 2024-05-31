#search for elements:

import numpy as n

x=n.array([10,20,30,40,50,20,70,20])
y=n.where(x==20)
print(y)

a=n.array([1,2,3,4,5,6,7,8])
b=n.where(a%2==0)
print(b)

c=n.where(a%2==1)
print(c)