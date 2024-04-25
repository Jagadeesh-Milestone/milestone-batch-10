#frozenset:
#it is the immutable version of set.
s={10,20,30,40,10}
a=frozenset(s)
print(a)
print(type(a))

b=a.copy()
print(b)

#b.add(100)
#print(b)

b=[10,20,30,40,50]
c=frozenset(b)
print(c)
print(type(c))
#c.append(100)
#print(c)

