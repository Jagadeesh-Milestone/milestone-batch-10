#add multiple records into a table:
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Chinna',
    database='users'
)
mycursor=mydb.cursor()
sql='INSERT INTO students(name,address) VALUES(%s,%s)'
values=[('hari','chennai'),('manoj','hyderabad'),('rupesh','mumbai'),
        ('naresh','hyderabad'),('suresh','chennai')]
mycursor.executemany(sql,values)
mydb.commit()
print(mycursor.rowcount,'records are added into a table')