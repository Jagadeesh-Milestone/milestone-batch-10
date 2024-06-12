#check for all the available databases
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Chinna'
)

mycursor=mydb.cursor()

sql='SHOW DATABASES'
mycursor.execute(sql)
for i in mycursor:
    print(i)

