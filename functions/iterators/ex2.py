l=[10,20,30,40]
m=l.__iter__()
a=m.__next__()
print(a)
b=m.__next__()
print(b)
c=m.__next__()
print(c)
d=m.__next__()
print(d)
#e=m.__next__()#stopIteration
#print(e)

m=[10,20,30]
n=iter(m)
print(next(n))
print(next(n))
print(next(n))
print(next(n))#stopIteration