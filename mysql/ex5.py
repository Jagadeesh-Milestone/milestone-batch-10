#primary key:
#while creating a table it is necessary to create a cloumn with unique key
#to each record.
#it will be done by defining PRIMARY KEY
#we can use "INT AUTO_INCREMENT PRIMARY KEY"
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Chinna',
    database='users'
)
mycursor=mydb.cursor()
sql='CREATE TABLE students(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(30),address VARCHAR(30))'
mycursor.execute(sql)
print('new table created successfully')