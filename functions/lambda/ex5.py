#nested lambda:
x=lambda a=100:(lambda b:a+b)
print(x())
result=x()
print(result(20))