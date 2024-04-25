#nested function:
#a function taking inside another function is called nested function.
#the main function is called outer function and the inside function is called
#inner function.

def d1():#outer function
    print('hello world')
    def d2():#inner function
        print('hello python learners')
    d2()
d1()