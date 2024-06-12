#add a new column into existing table
import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Chinna',
    database='users'
)
mycursor=mydb.cursor()
sql='ALTER TABLE employeedetails ADD COLUMN (id INT AUTO_INCREMENT PRIMARY KEY)'
mycursor.execute(sql)
print('table alterd successfully')