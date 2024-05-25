#method overloading
#python does not supports method overloading.
class milestone:
    def d1(self,a,b):
        print(a,b)
    def d1(self,a,b,c):
        print(a,b,c)
obj1=milestone()
obj1.d1(10,20)
