
class rbi:
    def rateofinterest(self):
        print('rbi gives money to the banks at 0% interest')
class icici(rbi):
    def rateofinterest(self):
        print('rate of interest in icici bank is 2%')
class hdfc(rbi):
    def rateofinterest(self):
        print('rate of interest in hdfc bank is 3%')
class axis(rbi):
    def rateofinterest(self):
        print('rate of interest in axis bank is 4%')
r=rbi()
r.rateofinterest()

a=axis()
a.rateofinterest()

h=hdfc()
h.rateofinterest()

i=icici()
i.rateofinterest()