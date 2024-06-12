#delete records:
import  mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Chinna',
    database='users'
)
mycursor=mydb.cursor()
sql='DELETE FROM students WHERE address="mumbai"'
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,'records are deleted')