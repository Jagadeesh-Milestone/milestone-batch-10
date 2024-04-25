#default argument value.
def d1(country='India'):
    print('I am from',country)
d1('australia')
d1('newzealand')
d1()
d1('srilanka')
d1()
#if you are passing the value to the argument that value will be taken
#if you are not passing any value to the argument default value will be taken

def d2(a,b=10):
    print(a+b)
d2(10,20)
d2(30)
d2(40,50)