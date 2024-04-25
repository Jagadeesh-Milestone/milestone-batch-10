#tuple:
#a tuple is a collection of data and this data may be anytype.
#tuple is taken in paranthesis().
#tuple allows duplicate values,index calling and index slicing.
#tuple is immutable meaning that once we create a tuple we cant modify the data.
#tuple is having ordered elements.
a=()
print(a)
print(type(a))

b=(10,10.3,5+6j,True,'bangalore')
print(b)
print(type(b))

#tuple allows duplicate values:
c=(10,20,30,10,20,10)
print(c)

#len:
d=(1,2,3,4,5,6)
print(len(d))

#count:
e=(100,200,300,100,200)
print(e.count(100))

#copy:
#we cant use copy in tuple.
f=(10,20,30,40)
#g=f.copy()
#print(g)

#clear:
g=(10,20,30)
#g.clear()
#print(g)

#index:
h=(10,20,30,40,50)
print(h.index(10))
#print(h.index(100))

#index calling:
i=(100,200,300,500)
print(i[0])
#print(i[5])

#concatenation:
#adding a tuple to another tuple is called concatenation.
j=(10,20,30,40)
k=(50,40,30,20,3)
print(j+k)
print(j+(100,200,300,400))
#we can only concatenate tuple to tuple but not tuple to list.

l=(10)
print(l)
print(type(l))

m=(10,)
print(m)
print(type(m))

#converting a list to tuple:
l=[10,20,30,40]
t=tuple(l)
print(t)
print(type(t))
#t.append(100)
#print(t)

#converting a tuple to list:
t=(1,2,3,4,5)
l=list(t)
print(l)
print(type(l))
l.append(1000)
print(l)

#index slicing:
s=(10,20,30,40,50)
print(s[0:3])