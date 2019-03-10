#Select everything and print it from a database table

#!/usr/bin/python3
import mysql.connector as mariadb

#Connect to database
mariadb_connection = mariadb.connect(host='your_host', user='your_user', password='your_pw', database='your_database')
cursor = mariadb_connection.cursor()
#Find and Print
cursor.execute("select *  from your_table")
results = cursor.fetchall()
print (results)

#Close connection
mariadb_connection.close()
