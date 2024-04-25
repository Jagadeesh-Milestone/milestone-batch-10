#sending a function as an argument value to another function:
def d1(a,b):
    return 'hello world',a,b
def d2(c):
    return 'hello python learners',c
def d3():
    return 'hello bangalore'
d=d1(d2(d3()),d3())
print(d)

d=d1(d3(),d3())
print(d)

d=d1(d2(d3()),d2(d3()))
print(d)