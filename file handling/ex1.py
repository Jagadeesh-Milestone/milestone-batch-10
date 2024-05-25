#file handling:
#file handling in python allows us to store the data that can be accessed by
#our code for various puposes like writing,reading,modifying and deleting a file.
#it allows us to treat a file as an object so that all the above operations
#can be performed on a file.
#creating and writing into a file:
f=open('hello.txt','w')
x=f.write('hello world')
print(x)
f.close()

#reading an existing file
f=open('hello.txt','r')
y=f.read()
print(y)
f.close()