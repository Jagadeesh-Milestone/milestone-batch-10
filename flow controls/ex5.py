#for loop:
#it is used when the user knows the exact output
#normally for loop is used on sequences
l=[10,20,30,40,50]
for a in l:
    print(a)

name='jagadeesh'
for i in name:
    print(i)

for i in range(100):
    print(i,end=",")
#break:
a=[10,20,30,40,50]
for i in a:
    print(i)
    if i==30:
        break
#continue:
b=[1,2,3,4,5,6,7,8]
for i in b:
    if i==4:
        continue
    elif i ==7:
        break
    print(i)