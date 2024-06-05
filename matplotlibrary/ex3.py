#line style and color
from matplotlib import pyplot
import pandas as p

x=p.array([1,5,8,3,10])
y=p.array([2,12,4,6,5])

#pyplot.plot(x,y,'o-r')
#pyplot.show()

#marker size
#pyplot.plot(x,y,'o',ms=30)
#pyplot.show()

#marker edge color:
#pyplot.plot(x,y,'D',ms=20,mec='#23FFAB')
#pyplot.show()

#marker face color:
pyplot.plot(x,y,'D',ms=15,mec='r',mfc='b')
pyplot.show()