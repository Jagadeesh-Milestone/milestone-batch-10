#polymorphism
#a single function/method having many forms

#polymorphism in * operator:
#* is used to multiplication
a=10
b=5
print(a*b)

#* is used in power
x=5
y=3
print(x**y)

#* is used in * args
def d1(*studennts):
    print(studennts)
d1('hari','naresh','suresh')

#** is used in **kwargs
def d2(**users):
    print(users)
d2(user1='hari',user2='naresh')

#polymorphism in oops:
class bird:
    def fly(self):
        print('some birds can fly some birds cannot fly')
class eagle(bird):
    def fly(self):
        print('an eagle can fly at very heights')
class parrot(bird):
    def fly(self):
        print('a parrot can fly but not at hieghts')
class ostrich(bird):
    def fly(self):
        print('an ostrich cannot fly')

o=ostrich()
o.fly()

p=parrot()
p.fly()

e=eagle()
e.fly()