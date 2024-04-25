#closure:
#a closure is a higher order function which satisfies the following three conditions.
#a function must be taken inside another function
#a function must be returned
#a function must be sent to a variable

def d1():
    def d2():
        return 'hello python'
    return d2()
d=d1()
print(d)