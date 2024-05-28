#date time:
#this module is used for displaying date and time using python
import datetime
a=datetime.datetime.now()
print(a)
#string format time
b=datetime.datetime(2000,8,27)
print(b.strftime("%B"))
#short form of week day
c=datetime.datetime.now()
print(c.strftime('%a'))
#full form of week day
d=datetime.datetime.now()
print(d.strftime('%A'))
#short form of month name
e=datetime.datetime.now()
print(e.strftime('%b'))
#full form of month name
f=datetime.datetime.now()
print(f.strftime('%B'))
#day of the month:
g=datetime.datetime.now()
print(g.strftime('%d'))
#day of the week:
h=datetime.datetime.now()
print(h.strftime('%w'))
#month number:
i=datetime.datetime.now()
print(i.strftime('%m'))
#short form of year:
j=datetime.datetime.now()
print(j.strftime('%y'))
#full form of year
k=datetime.datetime.now()
print(k.strftime('%Y'))
#hours possible values are 00-23
l=datetime.datetime.now()
print(l.strftime('%H'))
#hours possible values are 00-12
print(l.strftime('%I'))
#AM/PM
print(l.strftime('%p'))
#minutes possible values are 00-59
print(l.strftime('%M'))
#seconds possible values are 00-59
print(l.strftime('%S'))
#micro seconds
#print(l.strftime('%f'))
#time zone
print(l.strftime('%Z'))
#day number of the year
print(l.strftime('%j'))
#week number of the year
print(l.strftime('%W'))
#local version of time and date
print(l.strftime('%c'))
#century:
print(l.strftime('%C'))
#local version of date
print(l.strftime('%x'))
#local version of time
print(l.strftime('%X'))