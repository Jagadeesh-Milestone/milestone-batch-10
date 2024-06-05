from matplotlib import pyplot
import numpy

x=numpy.array([1,5,8,3,10])
y=numpy.array([2,12,4,6,5])

#pyplot.barh(x,y,color='r')#horizontal bar graph
pyplot.bar(x,y)#vertical bargraph
pyplot.show()