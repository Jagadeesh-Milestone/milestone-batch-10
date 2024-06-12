#order by
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Chinna',
    database='users'
)
mycursor=mydb.cursor()
#sql='SELECT * FROM students ORDER BY name'
#sql='SELECT * FROM students ORDER BY address'
#sql='SELECT * FROM students ORDER BY name DESC'
#sql='SELECT * FROM students ORDER BY address DESC'
sql='SELECT * FROM students ORDER BY id DESC'
mycursor.execute(sql)
result=mycursor.fetchall()
for i in result:
    print(i)