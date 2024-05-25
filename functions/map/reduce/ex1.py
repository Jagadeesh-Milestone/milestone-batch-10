#reduce:
#it is used to reduce a sequence into a single object:
#to use reduce we have to import it from functools
from functools import reduce

x=[10,20,30,40,50]
def d1(m,n):
    return m+n
y=reduce(d1,x)
print(y)
