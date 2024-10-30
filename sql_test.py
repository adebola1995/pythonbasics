import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="kaka",
    database="classicmodels",
    port=3306
)
if(connection.is_connected()):
    print("yipee!! DB is connectedo!")
else:
    print("DB could not be connected to")