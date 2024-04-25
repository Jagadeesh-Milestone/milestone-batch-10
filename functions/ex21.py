#globals method
#it is used to access global variable locally when global variable and local
#variable having same variable name.
x=100
print('x value before the function',x)
def d1():
    x=200
    print('x value in the function',x)
    print('x value before the function',globals()['x'])
d1()
print('x value after the function',x)