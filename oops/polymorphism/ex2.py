#polymorphism:
class vehicle:
    def transport(self):
        print('vehicles are used to transportation ')
class car(vehicle):
    def transport(self):
        print('a car is used to travel on roads')
class aeroplane(vehicle):
    def transport(self):
        print('an aeroplane is used to travel on air')
class ship(vehicle):
    def transport(self):
        print('a ship is used to travel on water')
s=ship()
s.transport()

a=aeroplane()
a.transport()

c=car()
c.transport()