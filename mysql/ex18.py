#DROP SCHEMA
import  mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Chinna',
    database='users'
)
mycursor=mydb.cursor()
sql='DROP SCHEMA hari'
mycursor.execute(sql)
print('one database is deleted')
#delete only if exists
sql='DROP SCHEMA IF EXISTS hari'
mycursor.execute(sql)
print('no such a database')
