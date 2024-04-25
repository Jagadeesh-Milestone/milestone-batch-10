#string
#a string is a collection of charaters
#in python any value that is taken in single or double quotes it will be treated
#as a string value:
a="bangalore"
print(a)
print(type(a))

b='hello'
print(b)
print(type(b))

c="10"
print(c)
print(type(c))

d='hello&*&87'
print(d)
print(type(d))

print(len(d))
print(d.count('l'))
print(d.count('z'))
print(d.index('&'))
print(d[-3])