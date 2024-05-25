#for loop in file handling:

f=open('java.txt','w')

for i in range(5):
    name=input('enter your name:')
    f.write(name)
    f.write('\n')
f.close()
print('data is stored')
