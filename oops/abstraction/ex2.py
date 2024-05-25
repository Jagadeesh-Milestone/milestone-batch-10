from abc import ABC,abstractmethod
class laptop(ABC):
    def __init__(self,brand,cost,year):
        self.brand=brand
        self.cost=cost
        self.year=year
    @abstractmethod
    def details(self):
        pass
class lenovo(laptop):
    def details(self):
        print('brand is',self.brand)
        print('cost is',self.cost)
        print('year is',self.year)
    def touchscreen(self):
        print('available')
class hp(laptop):
    def details(self):
        print('brand is',self.brand)
        print('cost is',self.cost)
        print('year is',self.year)
    def touchscreen(self):
        print('touch screen is not available')
obj1=hp('hp12',40000,2024)
obj1.details()
obj1.touchscreen()

obj2=lenovo('lenovol2',45000,2024)
obj2.details()
obj2.touchscreen()

obj3=laptop()
obj3.details()