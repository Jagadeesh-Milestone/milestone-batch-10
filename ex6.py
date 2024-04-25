#dictionary:
#a dictionary is collection of keys and value pairs.
#dict  is a mutable and having ordered key and values
#we can pass duplicate values but not keys

#empty dictionary:
a={}
print(a)
print(type(a))

#dictionary;
b={'name':'jagadeesh','address':'bangalore','contact':8908908908}
print(b)
print(b.keys())
print(b.values())
print(b.items())

print(b['name'])
print(b['contact'])

#add new key and value:
b['course']='python'
print(b)

b['contact']=7890789078
print(b)

#pop:
#it is used to remove a key and its value:
b.pop('address')
print(b)

#popitem:
#it is used to remove the last item.
b.popitem()
print(b)

#we cant take duplicate keys:
c={'name':'hari','name':'jagadeesh'}
print(c)

#we can take duplicate values:
d={'name1':'hari','name2':'hari'}
print(d)

del d['name1']
print(d)

#del d
#print(d)

#copy:
x=b.copy()
print(x)

#clear:
#b.clear()
#print(b)

#get:
print(b.get('name'))
print(b.get('contact'))

