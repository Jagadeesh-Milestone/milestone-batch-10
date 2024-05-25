#encapsulation:
#it is one of the oops concepts.it is the property in which wrapping up of data
# and methods into a single entity.
class milestone:
    def __init__(self):
        self._a=10
class python(milestone):
    def __init__(self):
        milestone.__init__(self)
        print('the value of a in milestone is',self._a)

        self._a=20
        print('the value of a in python is',self._a)
x=python()
y=milestone()
print('the value of a in python is',x._a)
print('the value of a in milestone is',y._a)