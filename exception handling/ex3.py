try:
    x=[10,20,40,50]
    print(x[0])
    print('statement one')
    print(x[2])
    y={10,20,30,40,50}
    y.remove(20)
    print(y)
except Exception:#if we have any errors in try block exception block will be executed
    print('statement two')
else:#if we dont have any errors in try block else block will be executed
    print('statement three')
finally:
    print('statement four')
#finally block will be executed in both the situations.
