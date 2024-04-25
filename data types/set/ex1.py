#set
#a set is a collection of data and this data may be anyt type
#set is having unordered elements.
#set dont allow duplicate values,index calling,index slicing
#set is taken in {}
#set is mutable,we can modify the data
a={10,10,2,True,'hello',5+6j}
print(a)
print(type(a))

b={10,20,30,40}
#print(b[0])
#print(b.index(10))

#add
#this method is used to add an element in the set
c={100,200,300}
c.add(500)
print(c)

#update:
#it is used to update the set with the elements
d={10,20,30,40}
d.update([100,200,300])
print(d)

#duplicate values are not allowed
e={10,20,30,10,20,40}
print(e)

#len
print(len(e))

#copy:
f={1,2,3,4}
g=f.copy()
print(g)

#clear:
h={100,200,300}
h.clear()
print(h)

#remove:
i={10,20,30,40}
i.remove(20)
print(i)

#discard:
j={1,2,3,4,5}
j.discard(3)
print(j)

#difference between remove and discard:
k={10,20,30,40,50}
#k.remove(100)
#print(k)

k.discard(100)
print(k)

#if we try to remove an element which is not in a set remove will raise an error
#but discard will not raise an error.

#pop:
l={10,20,30,40,5+6j}
l.pop()
print(l)

#union:
#it is used to print different elements in two sets
m={10,20,30,40,50,70}
n={100,200,10,20,60,70}
print(m.union(n))

#intersection:
print(m.intersection(n))

#difference:
print(m.difference(n))

#is subset

a={10,20,30,40}
b={10,20,30,40,50,60}
print(a.issubset(b))

#is superset:
print(b.issuperset(a))

#is disjoint:
c={1,2,3,4}
d={10,20,30,40}
print(c.isdisjoint(d))