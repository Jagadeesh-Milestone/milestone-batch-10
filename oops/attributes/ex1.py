#attributes:
#attributes are the variables belongs to a class
#there are three types of attriutes
#class attribute
#instance attribute
#static attribute
#class attribute:
class milestone:
    name='jagadeesh'
x=milestone.name
print(x)

#instance attribute:
class python:
    def d1(self):
        name='hari'
        print(name)
y=python()
y.d1()

#static attribute:
class java:
    @staticmethod
    def d2():
        name='arshad'
        print(name)
z=java()#instance creation
z.d2()

a=java.d2()#calling with class name
print(a)