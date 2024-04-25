#list:
#a list is a collection of data and this data may be any type.
#a list allows duplicate values,index calling,index slicing
#list having ordered elements
#list is taken in []
#list is mutable meaning that once we create a list we can modify the data.
l=[]
print(l)
print(type(l))

a=[10,20.9,5+6j,'hello',True]
print(a)
print(type(a))

#list allows duplicate values
b=[10,20,30,10,20,10]
print(b)

#count:
#it is used to find the no of apperance of each element in a list.
c=[1,2,3,1,2,1,3]
print(c.count(1))

#len:
#it is used to find the length of a list.
d=[100,200,300,40,6,6,40,'hello']
print(len(d))

#copy:
#it is used to store a copy of a list:
e=[10,20,30,40]
f=e.copy()
print(f)

#clear:
#it is used to clear the list elements.
g=[11,12,13,14]
g.clear()
print(g)

#append:
#it is used to add an element at the end of a list.
h=[10,20,30,40]
h.append(100)
print(h)

#index position:
#the index position of first element is always 0,next element is 1,...
i=[100,200,300,400]
print(i.index(100))

#index calling:
j=[10,20,30,40]
print(j[0])
print(j[2])
#print(j[5])

#negative index:
#the negative index of the last element is -1,before last element is -2,...
k=[1,2,3,4,5,6]
print(k[-1])
print(k[-3])

#pop:
#it is used to remove an element from the end of a list
l=[10,20,30,40,60]
#l.pop()
#print(l)
#if you want to pop a particular element we use index position
l.pop(-3)
print(l)

#extend:
#it is used to add multiple elements at the end of a list
m=[1,2,3,4,5]
m.extend([100,200,300])
print(m)

#insert:
#it is used to insert an element at a particular index position.
n=[100,200,300,400]
n.insert(3,10)
print(n)

#remove:
#it is used to remove an element from a list.
o=[10,20,30,40]
o.remove(20)
print(o)

#reverse:
#it is used to reverse the list elements.
p=[100,20,300,400,40,20,10]
p.reverse()
print(p)

#sort:
#it is used to print the list elements in ascending or decending order.
q=[40,30,50,10,70,20]
q.sort()
print(q)

q.sort(reverse=True)
print(q)