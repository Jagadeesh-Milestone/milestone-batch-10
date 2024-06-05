#pandas
#pandas library is used to work with data sets
#it is mainly used in data science
#it was invented by wes mc kinney in 2008
#to work with pandas we have ti import it
#we can give alias name also
import  pandas
print(pandas.__version__)

import pandas as p
print(p.__version__)

x=p.Series((10,20,30,40))
print(x)
print(type(x))
print(x[0])

y=p.Series([100,200,300,400],index=['a','b','c','d'])
print(y)
print(y['b'])
#print(y['z'])#key error