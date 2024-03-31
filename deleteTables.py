import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="AwmingPOS123",
    database = "Awming"
)

mycursor = mydb.cursor()

#mycursor.execute("DROP Table Inventory")
#mycursor.execute("DROP Table Incoming")
mycursor.execute("DROP Table Sales")
mycursor.execute("CREATE Table Sales (Transaction_No INT, Items VARCHAR(255), Total_Paid INT, Date DATE, Time TIME)")

#mycursor.execute("DROP Table Outgoing")

#mycursor.execute("ALTER TABLE Sales DROP COLUMN Barcode")

