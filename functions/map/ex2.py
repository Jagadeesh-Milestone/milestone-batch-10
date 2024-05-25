#without mapping:

a=[10,20,30,40,50,60,70]
b=[1,2,3,4,5,6]

def d1(x,y):
    return x*y
c=map(d1,a,b)
print(list(c))

#using lambda:
d=map(lambda f,g:f*g,a,b)
print(tuple(d))