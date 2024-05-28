# loops to Nested FOR loops
names=["GRk","python","institute"]
for i in names:
    print(i[0])

print("\n")
for i in names:
    print(i[0]+i[-1])

print("\n")

result = []
for i in names:
    result.append( i[0]+i[-1] )
print(result)

print("\n")

names=["GRk","python","institute"]
result = ['Gk', 'pn', 'ie','xyz']
data = [12, 13 , 0]

each_var = []
for each_name in names:

    for each_res in result:

        for each_num in data:

            each_var.append(each_name + each_res +str(each_num))

print(each_var)


