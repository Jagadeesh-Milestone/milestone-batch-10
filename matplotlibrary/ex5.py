from matplotlib import pyplot
import numpy

x=numpy.array([1,5,8,3,10])
y=numpy.array([2,12,4,6,5])

#pyplot.plot(x,linestyle='dotted',color='r',linewidth='10')
#pyplot.show()
pyplot.title('my data')
pyplot.xlabel('year')
pyplot.ylabel('population')
#pyplot.plot(x,y)
pyplot.grid()
pyplot.show()
