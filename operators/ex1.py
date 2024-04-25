#operators:
#these are used to perform operations on python objects and its values.
#python supports 7 types of operators.
#arithemetic operators
#assignment operators
#logical operators
#relational operators
#membership operators
#identity operators
#bitwise operators

#arithemetic operators
#these are used to perform basic mathematical operations
a=10
b=5
print(a+b)#addition
print(a-b)#subraction
print(a*b)#multiplication
print(a/b)#division
print(a//b)#floor division.it will takes 3.1--3.9 as 3
print(a%b)#modulus it stores the reminder value
print(a**b)#power

#assinment operators
x=15
x+=1
print(x)

y=10
y-=2
print(y)

z=20
z*=2
print(z)

#relational operators
d=10
e=20
print(d<e)
print(d>e)
print(d==e)
print(d!=e)
print(d<=e)
print(d>=e)

#logical operators
#and
#and returns True if both the statements are True otherwise it returns False.
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print('hello world')
x=10
y=20
print(x<y and y>x)
print(x<y and y<x)
print(x>y and y>x)
print(x>y and y<x)
print('hello bangalore')
#or
#or returns True if any one of the statement is True otherwise it returns False.
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print('hello world')
x=10
y=20
print(x<y or y>x)
print(x<y or y<x)
print(x>y or y>x)
print(x>y or y<x)

#not
#it returns opposite of the given statement
print(not True)
print(not False)

#membership operators
#It is used to check the availability of an item in the sequence
studentlist=['jagadeesh','hari','manoj','suresh']
print('hari' in studentlist)
print('mahesh' in studentlist)
print('jagadeesh' not in studentlist)
print('rupesh' not in studentlist)

#identity operators
#these are used to compare the id of an objects
x=[10,20,30,40,50]
y=[10,20,30,40,50]
z=x
print(id(x))
print(id(y))
print(id(z))
print(x is y)
print(y is z)
print(x is z)
print(x is not y)
print(y is not z)
print(z is not x)

#bitwise operators:
#these are used to compare the bits of an objects
#bitwise &
a=13
b=10
print(a&b)
print(bin(a))
print(bin(b))
print(bin(8))
0b1101
0b1010
#========
0b1111
#0b1000--8
#bitwise |
print(a|b)
print(bin(15))