import mysql.connector

mydb = mysql.connector.connect(
  host="db",
  user="root",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)