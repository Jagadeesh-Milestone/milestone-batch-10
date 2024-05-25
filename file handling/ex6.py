#pickling:
#it is the process of converting python object to byte stream code
#we use dump method in pickling
#to work with pickling we have to import it.
import pickle
f=open('jagadeesh.dat','wb')
x=[10,20,30,40,50]
y=pickle.dump(x,f)
print(y)
f.close()

