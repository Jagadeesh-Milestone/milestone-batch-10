#methods
#methods are the functions of a class
#there are three types of methods
#class method
#instance method
#static method

#instance method:
class milestone:
    productid=123456
    def product(self):
        productname='samsung'
        productcost=20000
        print('product name is',productname)
        print('product cost is',productcost)
        print('product id is',self.productid)
        print('product id is',milestone.productid)
x=milestone()
x.product()