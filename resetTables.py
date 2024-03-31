import mysql.connector

mydb = mysql.connector.connect(
     host="localhost",
    user="root",
    password="AwmingPOS123",
    database="Awming"
)

mycursor = mydb.cursor()

sql = "UPDATE Inventory SET Stocks = 0"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")

mycursor.execute("TRUNCATE TABLE Sales")
print(mycursor.rowcount, "record(s) affected")

mycursor.execute("TRUNCATE TABLE Incoming")
print(mycursor.rowcount, "record(s) affected")

mycursor.execute("TRUNCATE TABLE Outgoing")
print(mycursor.rowcount, "record(s) affected")