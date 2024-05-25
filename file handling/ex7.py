#unpickling:
#the process of converting byte stream code to python object
#we use load method in unpickling
import pickle
f=open('jagadeesh.dat','rb')
l=pickle.load(f)
print(l)
f.close()