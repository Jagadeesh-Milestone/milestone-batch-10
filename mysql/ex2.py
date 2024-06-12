#create a new database
import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Chinna'
)
mycursor=mydb.cursor()

sql='CREATE DATABASE users'
mycursor.execute(sql)
print('one database created successfully')