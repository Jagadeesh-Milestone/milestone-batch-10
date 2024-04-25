#use of closure:
#by using closure function even if we delete the main function we can use its
#functionality.
def d1():
    return 'hello world'
d=d1()
print(d)
del d
#print(d)
def d2():
    def d3():
        print('hello python learners')
    return d3
d=d2()
d()
del d2
d()
d()
d()