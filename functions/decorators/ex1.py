#decorators:
#decorators are the higher order python functions.
#we use @ annotation as a decoractor.
#decoractors are used to add some extra functionality to the already existing
#function.
# function without decorator
def d1(func):
    def d2():
        result=func()
        return result+'world'
    return d2
def d3():
    return 'hello'
d=d1(d3)
print(d())
