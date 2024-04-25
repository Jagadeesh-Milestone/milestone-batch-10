#while loop:
#it is used when the user doesnot knows the exact output:
i=0
while i<10:
    print(i)
    i+=1
#the loop will be repeated upto the given condition is true.
#whenever the condition becomes false the loop will be terminated.

#break statement:
#it is used to break the loop at a particular statement.
a=0
while a<20:
    print(a)
    if a==14:
        break
    a+=1
#continue statement:
#it is used to skip the current condition and continue with the other conditions
b=0
while b<10:
    b+=1
    if b==6:
        continue
    print(b)


