#regular expressions:
#it is used to make a search pattern which forms a sequence
#to work with regular expression python provides a module named 're'.
import re

#findall:
#it returns all the sequences in a list:
txt='hello python learners'
x=re.findall('l',txt)
print(x)

#if there is no match empty list will be returned
y=re.findall('z',txt)
print(y)

#^
#it is used to check whether the string is starting with the given characters
# or not
txt='hello java learners'
a=re.findall('^hello',txt)
print(a)

#$
#it is used to check whether the string is ending with the given characters
#or not
txt='hello bangalore'
b=re.findall('ore$',txt)
print(b)

#[a-m]
#it returns all the matches between a-m in a string
text='hello python learners'
c=re.findall('[a-m]',text)
print(c)

#[0-9]
#it returns all the numbers between 0-9 in a string
text='i am user 1122 my contact is 8989898998'
d=re.findall('[0-9]',text)
print(d)
