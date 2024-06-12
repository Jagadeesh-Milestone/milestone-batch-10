#delete the table:
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password="Chinna",
    database='users'
)
mycursor=mydb.cursor()
#sql='DROP table employeedetails'
sql='DROP table IF EXISTS employeedetails'
mycursor.execute(sql)
print('no such a table')