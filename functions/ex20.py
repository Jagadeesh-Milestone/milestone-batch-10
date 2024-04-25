#local variable:
#once we declare a variable locally we can use it within that scope only

#print('x value before the function',x)
def d1():
    x=200
    print('x value in the function',x)
    print('x value inside the function',x)
d1()

#print('x value after the function',x)