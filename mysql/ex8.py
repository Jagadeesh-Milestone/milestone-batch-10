#add a record into a table
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Chinna',
    database='users'
)
mycursor=mydb.cursor()

sql='INSERT INTO users(name,address) VALUES (%s,%s)'
values=('jagadeesh','bangalore')
mycursor.execute(sql,values)
mydb.commit()
print('one record added successfully')