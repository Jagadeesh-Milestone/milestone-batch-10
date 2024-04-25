#multiple expressions:
def d1(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
d1(10,20)

#using lambda:
x=lambda c,d:((c+d),(c-d),(c*d),(c/d))
print(x(20,30))