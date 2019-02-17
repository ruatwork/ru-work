# This connects to a database in separate server, and writes into it

#!/usr/bin/python3
import mysql.connector as mariadb
var1='random_variable'
var2='random_variable2'
# Connect to MariaDB
mariadb_connection = mariadb.connect(host='your_ip', user='your_dbuser', password='your_pw', database='your_database')
cursor = mariadb_connection.cursor()

# Insert a new row to a table
try:
	cursor.execute("insert into your_table (name,address) values (%s, %s)", (var1, var2))
except mariadb.Error as error:
	print("Error: {}".format(error))

# Commit changes to table, autocommit is disabled by default
mariadb_connection.commit()
print ("The last inserted id was: "),cursor.lastrowid

# Close connection to MariaDb
mariadb_connection.close()

