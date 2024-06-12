#update records:
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Chinna',
    database='users'
)
mycursor=mydb.cursor()
#sql='UPDATE students SET address="delhi" WHERE address="chennai"'
sql='UPDATE students SET address="delhi" WHERE id="7"'
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,'rows are updated')