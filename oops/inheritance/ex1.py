#inheritance:
#it is the one of python oops concepts
#inheritance is the property in which one class is getting all the attributes
#and methods of an another class.
#here the class which is inherited is called child/sub/derived class.
#the class from where the class is inherited is called parent/super/base class.
#python supports five types of inheritance:
#single level inheritance
#multi level inheritance
#multiple inheritance
#hirercheal inheritance
#hybrid inheritance

#single level inheritance:
#when a single child class is derived from a single parent class then the
#property is called single level inheritance.

class parent:
    money=10000
    print(money)
    def d1(self):
        print('i am the parent property')
class child(parent):
    money=5000
    print(money)
    def d2(self):
        print('i am a child property')
c=child()
c.d2()
c.d1()