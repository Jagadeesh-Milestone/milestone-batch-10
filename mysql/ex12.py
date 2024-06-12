#filter by using wildcard characters
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Chinna',
    database='users'
)
mycursor=mydb.cursor()

#sql='SELECT * FROM students WHERE name LIKE "%sh%"'
#sql='SELECT * FROM students WHERE address LIKE "%ai%"'
sql='SELECT * FROM students WHERE id LIKE "%1%"'
mycursor.execute(sql)
result=mycursor.fetchall()
for i in result:
    print(i)