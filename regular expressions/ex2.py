#search method searches for a matching object
#if no match is found none will be returned
import  re
text='hello7 python6 learners'
a=re.search('^hello',text)
print(a)

b=re.search('^llo',text)
print(b)

c=re.search('learners$',text)
print(c)

d=re.search('[0-9]',text)
print('the first number is located at',d.start())

#e=re.search("\S",text)
#print(e.start())

#split:
#it is used to split the string at each match:
txt='hello python learners'
a=re.split('l',txt)
print(a)

b=re.split('l',txt,2)
print(b)

#sub:
#it is used to replace a match with other characters
txt='my name is hari i am learning python'
a=re.sub('a','c',txt)
print(a)

b=re.sub('a','z',txt,2)
print(b)