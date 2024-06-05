import  pandas as p

data={"name":['emp1','emp2','emp3'],"salary":[15000,20000,25000]}
x=p.DataFrame(data)
print(x)
print(x.loc[1])

y=p.DataFrame(data,index=['user1','user2','user3'])
print(y)
print(y.loc['user3'])