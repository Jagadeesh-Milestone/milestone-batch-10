#create a new table.
import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Chinna',
    database='users'
)
mycursor=mydb.cursor()

sql='CREATE TABLE users(name VARCHAR(30), address VARCHAR(40))'

mycursor.execute(sql)
print('new table created successfully')