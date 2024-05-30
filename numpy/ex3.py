#accessing elements from one dimensional array
import  numpy as n
x=n.array([10,20,30,40])
print(x[0])
print(x[-1])
print(x[0]+x[-2])

#accessing elements from two dimensional array
y=n.array([[1,2,3,4],[5,6,7,8]])
print(y[0])
print(y[1])
#print(y[2][2])

#accessing elements from three dimensional array
z=n.array([[[1,2],[3,4]],[[5,6],[7,8]],[[9,10],[11,12]]])
print(z[0])
print(z[1])
print(z[0][0])
print(z[1,1])
print(z[0,0,0])
print(z[1,1,1])