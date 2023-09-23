import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Gbogo@israel321',
)


cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE dbname")

print("Database Connected Successfully!")