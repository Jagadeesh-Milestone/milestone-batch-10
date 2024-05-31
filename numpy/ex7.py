#iterating over numpy array:
import  numpy as n
#iterating over one dimensional array:
x=n.array([10,20,30,40,50])
for i in x:
    print(i)
#iterating over two dimensional array:
y=n.array([[10,20,30],[40,50,60]])
for i in y:
    for j in i:
        print(j)
#nditer:
z=n.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for i in n.nditer(z):
    print(i)

#ndennumerate:
x=[10,20,30,40]

for x,y in n.ndenumerate(x):
    print(x,y)