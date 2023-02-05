import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='my_password'
)

mycursor = mydb.cursor()
mycursor.execute('CREATE DATABASE my_first_db')
