import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "user",
    password = "darun"
)
print (mydb)