#method overriding:
class parent:
    def mobile(self):
        print('I will give 10000 to buy a mobile')

class child(parent):
    def mobile(self):
        print('I will buy mobile for 20000')
c=child()
c.mobile()