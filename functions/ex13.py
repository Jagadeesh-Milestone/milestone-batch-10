#we can use the arguments of inner function within the inner function only.
#we cant use them outside the inner function.
def d1():
    #print(a+b)
    def d2(a,b):
        print(a+b)
    d2(10,20)
    #print(a+b)
d1()