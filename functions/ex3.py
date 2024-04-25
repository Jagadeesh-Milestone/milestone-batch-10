#* args
#if you dont know how many values you are passing just put a * before the argument
#name.
#if you want to pass multiple values to a single argument put a * before the
#argument name.
def d1(*users):
    print(users)
    print('second user name is',users[1])
d1('hari','jagadeesh','mahesh','naresh')