#multi level inheritance:
#when more than one base class and one derived class are there then it is called
#multi level inheritance.
class grandparent:
    def d1(self):
        print('i am a grand parent property')
class parent(grandparent):
    def d2(self):
        print('i am a parent property')
class child(parent):
    def d3(self):
        print('i am a child property')
c=child()
c.d3()
c.d2()
c.d1()