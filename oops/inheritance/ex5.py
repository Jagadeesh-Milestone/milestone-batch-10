#hybrid inheritance
#it is the combination of two or more inheritances:
class grandparent:
    def d1(self):
        print('i am a grand parent property')
class parent(grandparent):
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
p.d1()