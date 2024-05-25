#set comprehension:
l=[1,2,3,2,4,3,5,5,6]
m=set()
for i in l:
    if i%2==1:
        m.add(i)
print(m)
#using comprehension
n={i for i in l if i%2==1}
print(n)

#generator comprehension:
x=(i for i in l if i%2==0)
print(x)
print(next(x))
print(next(x))
print(next(x))

for i in x:
    print(i)