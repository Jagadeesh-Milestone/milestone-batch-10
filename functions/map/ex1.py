#map:
#python object mapping with another object is called map
#it is a python builtin function
#without mapping:
l=[10,20,30,40,50]
print(l*2)
for i in l:
    print(i*2)

#using map function:
#syntax--map(function name,iterable)
def d1(n):
    return n*2
x=map(d1,l)
#print(x)
#for i in x:
  #  print(i)
print(set(x))

#map using lambda function:
y=map(lambda d:(d*3),l)
print(list(y))