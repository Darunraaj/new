import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "darun",
    database = "demo"
)
mycursor = mydb.cursor()
sql = "insert into customers (customer_name , customer_age , address) values (%s,%s,%s)"
val = [("darun", 21 , "TN"),
       ("naveen" , 20 , "TN")]
mycursor.executemany(sql , val)
mydb.commit()
print (mycursor.lastrowid, "record inserted.")
#for db in mycursor:
#    print (db)