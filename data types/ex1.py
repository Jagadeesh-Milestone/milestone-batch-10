#data type:
#it is the type of data which we are passing to variable.
#python supports 6 types of data types:
#number datatypes--int,float,complex
#sequences--list,tuple,range,strings
#boolen --True and False
#mapping--dictionary
#set--set,frozenset
#binary datatypes--bytes,bytearray

#number data types:
#int:
#in python any real number will be treated as an integer value.
a=100
print(a)
print(type(a))

#float:
#in python any decimal value will be treated as a float value.
b=10.8
print(b)
print(type(b))

#complex numbers:
#it is the combination of a real number and an imaginary number:
c=4+6j
d=5j
print(c)
print(d)
print(type(c))
print(c.imag)
print(c.real)
print(d.imag)
print(d.real)
e=5-6j
print(e)
print(e.real)
print(e.imag)

#binary numbers:
#they starts with 0b.
#its base value is 2
#possible values are 0,1
f=5
print(bin(f))

#hexa decimal numbers:
#they starts with 0x
#its base value is 16
#possible values are 0-9,a-f.
g=17
print(hex(g))

h=0xa
print(h)

#octal numbers:
#they strats with 0o
#its base value is 8
#posible values are 0-7.
i=24
print(oct(i))

j=0o31
print(j)

