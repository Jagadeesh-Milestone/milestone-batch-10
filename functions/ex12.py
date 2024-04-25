#we can use the arguments of outer function in outer fuction as well as
#in inner function
def d1(a,b):
    print(a+b)
    def d2():
        print(a+b)
    d2()
    print(a+b)
d1(10,20)