import pandas

x=pandas.read_csv('data.csv')
print(x.head())
print(x.tail(10))
print(x.info())

y=x['Duration'].mean()
print('mean of duration is:',y)

z=x['Duration'].median()
print('median of z is:',z)

a=x['Duration'].mode()
print(a)