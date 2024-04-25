#using for loop in generator:

def d1(n):
    for i in range(n):
        yield i
d=d1(4)
#print(next(d))
#print(next(d))
#print(next(d))
#print(next(d))
#print(next(d))

for i in d:
    print('hello world')
    print(i)

def d2():
    yield 100
    return 200
    yield 300
d=d2()
print(next(d))
#print(next(d))
# we cant use return statement in generators

x=(i for i in range(10))
print(x)
print(type(x))#generator
y=list(x)
print(y)
print(type(y))#list