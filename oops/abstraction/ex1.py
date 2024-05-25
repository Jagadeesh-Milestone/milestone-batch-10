#abstraction:
#it is the process of hiding the unnecessary information and displaying the
#necessary information.
#to use abstraction we have to import it from abc
from abc import ABC,abstractmethod
class polygon(ABC):
    @abstractmethod
    def sides(self):
        print('polygon has many sides')
class triangle(polygon):
    def sides(self):
        print('a triangle has three sides')
class square(polygon):
    def sides(self):
        print('a square has four sides')
class pentagon(polygon):
    def sides(self):
        print('a pentagon has five sides')
obj1=pentagon()
obj1.sides()

obj2=square()
obj2.sides()

obj3=triangle()
obj3.sides()

obj4=polygon()#it cannot be accessed since it is taken in abstract method
obj4.sides()