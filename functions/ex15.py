#we can use only a single return in a function.
def d1():
    return 'hello world'
    return 'hello bangalore'
    return 'hello python'
print(d1())

#returning a function:
def d2():
    def d3():
        return 'hello python learners'
    return d3()
d=d2()
print(d)