#select the records by filter;
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Chinna',
    database='users'
)
mycursor=mydb.cursor()
#sql="SELECT * FROM students WHERE username='naresh'"
#sql='SELECT * FROM students WHERE address="hyderabd"'
sql='SELECT * FROM students WHERE id=4'
mycursor.execute(sql)
result=mycursor.fetchall()
for i in result:
    print(i)