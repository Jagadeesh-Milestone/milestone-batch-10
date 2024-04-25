#find the recursion limit
import sys
print(sys.getrecursionlimit())

#change the recursion limit
x=sys.setrecursionlimit(500)
print(sys.getrecursionlimit())

i=1
def d1():
    global i
    print('hello world',i)
    i+=1
    d1()
d1()