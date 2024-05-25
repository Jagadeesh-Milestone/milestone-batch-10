#append:
#if we are not using append method then the data in a file will be deleted
#and new data will be added.

f=open('python.txt','a')
x=f.write('hello bangalore')
print(x)
f.close()