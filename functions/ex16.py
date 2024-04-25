#sending one function as an argument value of another function.
def d1(a):
    return 'hello world',a
def d2():
    return 'hello milestone'

d=d1(d2())
print(d)


