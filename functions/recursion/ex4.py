#factorial of a number using recursion:
def factorial(n):
    if (n==1 or n==0):
        return 1
    else:
        return (n*factorial(n-1))

x=5;
print('the number is ',x)
print('factorial of :',x, 'is ',factorial(x))

