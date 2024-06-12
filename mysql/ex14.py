#limit the result
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Chinna',
    database='users'
)
mycursor=mydb.cursor()
#sql='SELECT * FROM students LIMIT 5'
#sql='SELECT * FROM students LIMIT 5 OFFSET 3'
#sql='SELECT * FROM students LIMIT 5 OFFSET 10'
#sql='SELECT * FROM students ORDER BY name LIMIT 3 '
#sql='SELECT * FROM students ORDER BY address LIMIT 5 OFFSET 3'
sql='SELECT * FROM students ORDER BY address DESC LIMIT 5 OFFSET 3'
mycursor.execute(sql)
result=mycursor.fetchall()
for i in result:
    print(i)