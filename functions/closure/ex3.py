def d1():
    l=[10,20,30,40,50]
    def d2():
        l.append(100)
        return l
    return d2
d=d1()
print(d())


