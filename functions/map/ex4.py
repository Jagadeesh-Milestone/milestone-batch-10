cities=['bangalore','hyderabad','chennai','mumbai']
#print(cities[::-1])
#cities.reverse()
#print(cities)
for i in cities:
    print(i[::-1])
def d1(n):
    return n[::-1]
c=map(d1,cities)
print(list(c))

#lambda:
m=map(lambda d:d[::-1],cities)
print(tuple(m))