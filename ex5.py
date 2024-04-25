#set:
#a set is a collection of data and this data may be anytype
#a set is having unordered elements
#set dont allow duplicate values,index calling and index slicing
#set is taken in {}
#set is mutable.
#set
a={10,10.2,'hello',True,5+6j}
print(a)
print(type(a))

#dont allows duplicate values
b={10,20,30,10,20,40}
print(b)

#len
print(len(b))

#copy:
c=b.copy()
print(c)

#clear:
b.clear()
print(b)

#add:
#it is used to add a single element into a set
d={10,20,30,40,50}
d.add(100)
print(d)

#update:
#it is used to update the set with multiple elements
e={100,200,300,400}
e.update([10,20,30])
print(e)

#remove:
f={10,20,30,40}
f.remove(20)
print(f)

#discard:
g={1,2,3,4}
g.discard(3)
print(g)

#difference betweeen remove and discard.
h={10,20,30,40}
#h.remove(100)
#print(h)

h.discard(200)
print(h)

#if we remove the element which is not in the set we get key error
#if we discard the element which is not in the set we dont get any error the
#actual set will be displayed.

#pop:
i={10,20,30,40,5+6j,True,50}
i.pop()
print(i)

#union:
a={10,20,30,40,50}
b={20,30,40,60,70}
print(a.union(b))

#intersection:
#it will display the common elements in two sets
print(a.intersection(b))

#is subset:
x={10,20,30,40}
y={10,20,30,40,50,60,70}
print(x.issubset(y))

#superset:
print(y.issuperset(x))

#is disjoint:
s={10,20,30,40}
t={50,60,70,80}
print(s.isdisjoint(t))

#difference:
d={10,20,30,40}
e={40,30,60,70}
print(d.difference(e))

#frozenset:
#it is the immutable verion of set:
s={10,20,30,40,50}
a=frozenset(s)
print(a)

#a.add(100)
#print(a)

b=a.copy()
print(a)

l=[10,20,30,40]
m=frozenset(l)
print(m)

#m.append(300)
#print(m)