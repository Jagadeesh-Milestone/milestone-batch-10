#** args
#if you want to pass keyword arguments put a ** before argument name
def d1(**students):
    print(students)
    print('the smartest student is',students['studenttwo'])
d1(studentone='hari',studenttwo='mahesh',studentthree='naresh')