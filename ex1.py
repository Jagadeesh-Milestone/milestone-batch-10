#sequences:
#list:
#a list is a collection/sequence of data and that data may be anytype.
#list is taken in [].
#list allows duplicate values,index calling and index slicing.
#list is having ordered elements.
#list is mutable meaning that once we create a list we can modify the data.
#empty list:
a=[]
print(a)
print(type(a))

#we can pass any data type:
b=[10,10.2,'hello',True,5+6j]
print(b)

#len():
#it is used to find the no of elements in a list.
c=[10,20,30,40,50]
print(len(c))

#it allows duplicate values:
d=[10,20,30,10,20,10]
print(d)

#count:
#it is used to find the no of appearance of each element.
print(d.count(10))
print(d.count(30))
print(d.count(100))

#index:
#the index position of first element is always 0,second is 1,...
e=[10,20,30,40]
print(e.index(10))
print(e.index(40))
#print(e.index(100))

print(e[0])
print(e[3])
#print(e[5])

#negative index:
#the negative index of last element is always -1,before element is -2,...
f=[10,20,30,30]
print(f[-1])
print(f[-3])
#print(f[-5])

#append:
#it is used to add an element at the end of a list:
g=[1,2,3,4,5,6]
g.append(10)
print(g)

#pop:
#it is used to remove last element from the list
h=[10,20,30,40]
h.pop()
print(h)

#we can remove particular element by using index position:
i=[100,200,300,400]
i.pop(0)
print(i)
i.pop(-1)
print(i)

#extend:
#it is used to add multiple elements at the end of a list:
j=[10,20,20,30]
j.extend([100,200,300])
print(j)

#insert:
# we can insert any value at a particular index position:
k=[10,20,40,50,60]
k.insert(2,30)
print(k)

#remove:
#it is used to remove an element from a list:
l=[10,20,30,40]
l.remove(30)
print(l)

#reverse:
#it is used to reverse the list elements:
m=[10,20,40,30,50]
m.reverse()
print(m)

#sort:
#it is used to print the list elements in ascending or descending order
n=[10,50,30,60,70,20]
n.sort()
print(n)
n.sort(reverse=True)
print(n)

#clear:
o=[10,20,30,50]
o.clear()
print(o)

#copy:
p=[10,20,30,40,40]
q=p.copy()
print(q)

#index slicing:
#it is used when you need a particular portion of a list.
#syntax--starting index:ending index-1:stepover.
l=[0,1,2,3,4,5,6,7,8,9,10]
print(l[2:8])
print(l[0:10])
print(l[6:2])
print(l[-6:-1])
print(l[-2:-8])
print(l[5:])
print(l[:8])
print(l[0:10:1])
print(l[0:10:2])
print(l[::3])
print(l[::-1])