#filter:
#it is used to filter the required objects/elements from the sequence
#filter is  a python builtin function:
l=[1,2,3,4,5,6,7,8,9,10]
for i in l:
    if i%2==0:
        print(i)
def d1(n):
    return n%2==1
x=filter(d1,l)
print(list(x))

#lambda
m=filter(lambda x:x%2==0,l)
print(tuple(m))