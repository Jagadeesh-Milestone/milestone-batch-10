#a function using decorator

def d1(func):
    def d2():
        result=func()
        return result+'world'
    return d2
@d1
def d3():
    return 'hello'
d=d3()
print(d)