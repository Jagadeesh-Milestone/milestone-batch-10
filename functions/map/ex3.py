#map:
cities=['bangalore','hyderabad','chennai','mumbai']
print(len(cities))
for i in cities:
    print(len(i))

#by using map:
def d1(n):
    return len(n)
x=map(d1,cities)
print(list(x))

#using lambda
y=map(lambda  b:len(b),cities)
print(tuple(y))