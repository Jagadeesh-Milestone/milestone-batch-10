#hireracheal inheritance:
#it is the property in which more than one child class are derived from a single
#parent class:
class grandparent:
    def d1(self):
        print('i am a grand parent property')
class parent(grandparent):
    def d2(self):
        print('i am a parent property')
class child(grandparent):
    def d3(self):
        print('i am a child property')
class milestone(grandparent):
    def d4(self):
        print('i am a milestone property')
c=child()
c.d3()
c.d1()

p=parent()
p.d2()
p.d1()

m=milestone()
m.d4()
m.d1()