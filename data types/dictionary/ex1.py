#dictionary:
#a dictionary is a collection of key and value pairs.
#a dict is mutable
#dict is ordered key and values
#dict keys cannot be duplicate but we can take duplicate values

#empty dictionary:
a={}
print(a)
print(type(a))

#dictionary
b={'name':'jagadeesh kumar','address':'bangalore','contact':8908908908}
print(b)
print(type(b))
print(b.keys())
print(b.values())
print(b.items())

#copy
c=b.copy()
print(c)

#pop:
#b.pop('address')
#print(b)

#popitem:
b.popitem()
print(b)

#update:
b.update({'name':'venkatesh'})
print(b)

b['address']='hyderabad'
print(b)

c=b.get('name')
print(c)

d=b.get('address')
print(d)

#clear:
b.clear()
print(b)

#formkeys:
x=('user1','user2','user3')
y='jagadeesh'
d=dict.fromkeys(x,y)
print(d)

#we cant use duplicate keys:
f={'user1':'jagadeesh','user1':'hari'}
print(f)

#we can use duplicate values:
g={'user1':'hari','user2':'hari'}
print(g)

#del
del g['user1']
print(g)

#del dict
del g
print(g)