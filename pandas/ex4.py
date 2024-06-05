import  pandas as p
x=p.read_csv('data.csv')
print(x)

y=x.head(100)
print(y)

z=x.tail(10)
print(z)

a=x.info()
print(a)

b=x['Duration'].mean()
print(b)

c=x['Pulse'].mean()
print(c)

d=x['Calories'].median()
print(d)

e=x['Pulse'].mode()
print(e)