#check for existing tables in a database
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Chinna',
    database='users'
)
mycursor=mydb.cursor()

sql='SHOW TABLES'
mycursor.execute(sql)

for i in mycursor:
    print(i)