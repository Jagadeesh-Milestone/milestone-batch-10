#varibles
#we have three types of variables in python
#local variables
#global variables
#protected variables

#global variables:
#if we declare a variable globally we can use it anywhere in the program.
x=100
print('x value before the function',x)
def d1():
    print('x value in the function',x)
d1()
print('x value after the function',x)