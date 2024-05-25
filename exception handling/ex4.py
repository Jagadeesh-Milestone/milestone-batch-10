#raise an exception:
number=int(input('please enter any number:'))
if number<=0:
    raise Exception('enter only positive numbers')
else:
    print(number)

x=5+6j
if type(x) is complex:
    raise Exception('dont take complex values')
else:
    print(x)