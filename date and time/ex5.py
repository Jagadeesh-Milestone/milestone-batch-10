from datetime import datetime

d=['23/06/15 03:34:55','22/04/12 06:37:56']

x='%d/%m/%y %H:%M:%S'

for i in d:
    print(datetime.strptime(i,x))