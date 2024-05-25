#multiple inheritance:
#it is the roperty in which one child class is deriving from more than one parent
#class
class grandparent:
    def d1(self):
        print('i am a grand parent property')
class parent:
    def d2(self):
        print('i am a parent property')
class child(parent,grandparent):
    def d3(self):
        print('i am a child property')
c=child()
c.d3()
c.d2()
c.d1()

p=parent()
p.d2()
