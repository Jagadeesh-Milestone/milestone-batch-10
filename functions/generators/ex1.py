#generators:
#these are the python functions which are used to store  a function and we can
#use it whenever we want it.
#instead of return we use yield keyword.
def d1(a,b):
    print(a+b)
d1(10,20)

def d2(c,d):
    return c+d
print(d2(30,40))
def d3(a,b):
    yield a+b
    yield a-b
    yield a*b
d=d3(10,20)
print(next(d))
print('hello world')
print(next(d))
print('hello bangalore')
print(next(d))
print(next(d))