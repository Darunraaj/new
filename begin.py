import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "darun"
)
print(mydb)
