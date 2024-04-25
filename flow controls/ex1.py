#flow controls/control statements/conditional statements.
#these are used to control the flow of a program.
#if
#else
#elif
#nested if
#while
#for

#if:
#if returns true if the given statement is true.
a=10
if a<20:
    print('hello world')

b=10
if a==b:
    print('hello bangalore')

x=20
if a==x:
    print('hello python learners')
#else:
#else will be executed if the if statement is False:
s=100
t=200
if s==t:
    print('if condition is executed')
else:
    print('else condition is executed')

#pass:
#it is used to fill empty blocks in python code.
r=10
d=20
if r==d:
    pass
else:
    print('else block is executed')

#name=input('please enter your name:')
#if name=='jagadeesh':
  #  print('hello',name)
#else:
  #  print('hey!',name,' you are not jagadeesh')

#user=input('enter user name:')
#pin=int(input('enter your pin:'))
#if user=='jagadeesh' and pin==5678:
  #  print('login success')
#else:
    #print('login failed')

#user=input('enter user name:')
#pin=int(input('enter your pin:'))
#if user=='jagadeesh' or pin==5678:
  #  print('login success')
#else:
   # print('login failed')

#elif:
#it is used to check the multiple statements at a time.
#whenever the condition becomes true that statement will be executed otherwise
#else statement will be executed.
game='cricket'
if game=='football':
    print('i dont like to play football')
elif game=='volleyball':
    print('i dont like to play volleyball')
elif game=='kabadi':
    print('i dont like play kabadi')
elif game=='cricket':
    print('i like to play cricket')
else:
    print('i dont like to play games')

#input in elif:
username=input('please enter your name:')
if username=='jagadeesh':
    print('hello',username)
elif username=='hari':
    print('hi',username)
elif username=='suresh':
    print('good evening',username)
elif username=='mahesh':
    print('welcome',username)
else:
    print('you are not a valid user')

user=input('please enter your username:')
l=['hari','manoj','suresh','naresh']
if user in l:
    print(user,'is in list')
else:
    print(user,'is not in list')

