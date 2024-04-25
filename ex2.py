#tuple:
#taken in ().
#tuple is immutable we cant modify the data.
#empty tuple:
a=()
print(a)
print(type(a))

#tuple
b=(10,10.2,'hello',True,10)
print(b)

#len:
print(len(b))

#count:
print(b.count(10))

#index:
print(b.index(10.2))
print(b[-2])

#index slicing:
t=(0,1,2,3,4,5,6)
print(t[0:4])

#append:
#t.append(100)

#concatenation:
#adding a tuple to another tuple:
s=(10,20,30,40)
m=(20,30,40)
print(s+m)
print(s+(100,200,300))

n=(10)
print(n)
print(type(n))

o=(10,)
print(o)
print(type(o))

#converting a list to tuple:
l=[10,20,30,40]
t=tuple(l)
print(t)
print(type(t))

#converting tuple to list:
t=(100,200,300)
l=list(t)
print(l)
print(type(l))