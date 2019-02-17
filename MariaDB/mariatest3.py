# This connects to a database in separate server, and writes into it

#!/usr/bin/python3
import mysql.connector as mariadb

# Connect to MariaDB
mariadb_connection = mariadb.connect(host='server_ip', user='your_user', password='your_pw', database='your_database')
cursor = mariadb_connection.cursor()

# Retrieve information from database
#some_name = 'Seppo'
#cursor.execute("select name,address from your_table where name=%s", (some_name,))

#for name, price in cursor:
#	print("Name: {}, Address: {}").format(name,address)

# Insert a new row to a table
try:
	cursor.execute("insert into your_table (name,address) values (%s,%s)", ('Turo Takkanen','445566'))
except mariadb.Error as error:
	print("Error: {}".format(error))

# Commit changes to table, autocommit is disabled by default
mariadb_connection.commit()
print ("The last inserted id was: "), cursor.lastrowid

# Close connection to MariaDb
mariadb_connection.close()

