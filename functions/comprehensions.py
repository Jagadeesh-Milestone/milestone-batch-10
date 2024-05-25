#comprehensions:
#in python comprehensions are used to create a new sequence with already
#existing sequence in a short and concise way.
#python supports 4 types of comprehensions
#list comprehension
#dictionary comprehension
#set comprehension
#generator comprehension
#list comprehension:
#creating a even numbers list using list of numbers without comprehension:
l=[1,2,3,4,5,6,7,8,9,10]
x=[]
for i in l:
    if i%2==0:
        x.append(i)
print(x)

#by using list comprehension:
#syntax--[var for var in list]
y=[i for i in l if i%2==1]
print(y)

#square of range of values without comprehension:
a=[]
for i in range(1,10):
    a.append(i*i)
print(a)

#using comprehension:
b=[i*i for i in range(1,10)]
print(b)