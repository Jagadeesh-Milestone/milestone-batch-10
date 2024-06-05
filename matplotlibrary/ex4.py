#line style:

from matplotlib import  pyplot
import  numpy

x=numpy.array([1,5,8,3,10])
y=numpy.array([2,12,4,6,5])

#pyplot.plot(x,y,linestyle='dashdot',color='r')
#pyplot.show()

pyplot.plot(x,linestyle='dotted',color='r')
pyplot.plot(y,linestyle='dashed',color='b')
pyplot.show()