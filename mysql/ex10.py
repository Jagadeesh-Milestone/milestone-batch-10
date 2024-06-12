#select the records from the table:
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Chinna',
    database='users'
)
mycursor=mydb.cursor()
sql='SELECT * FROM students'
mycursor.execute(sql)
#result=mycursor.fetchall()
#result=mycursor.fetchone()
#result=mycursor.fetchmany(5)
#print(result)
#select particular columns:
#sql='SELECT id,address FROM students'
#mycursor.execute(sql)
#result=mycursor.fetchall()
#for i in result:
   # print(i)