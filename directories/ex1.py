#directories:
#a directory is a collection of files and subdirectories.
#a directory inside another directory is called subdirectory.
#python has a module named 'os' to work with directories.
import  os

#get current working directory:
#a=os.getcwd()
#print(a)

#make a new directory:
#b=os.mkdir('python')
#print(b)

#make a subdirectory:
#c=os.mkdir('html/java')
#print(c)

#make a directory and subdirectory
#d=os.makedirs('jagadeesh/hari')
#print(d)

#rename the existing directory:
#e=os.rename('python','html')
#print(e)

#rename the subfolder:
#f=os.renames('jagadeesh/hari','milestone')
#print(f)

#remove subdirectory:
#g=os.rmdir('html/java')
#print(g)

#remove directory and subdirectory
#h=os.removedirs('html/java')
#print(h)

import functools
print(dir(functools))
print(dir(list))
print(dir(set))