# This will connect to separate server, not working yet

#!/usr/bin/python
import mysql.connector as mariadb

# Connect to MariaDB
mariadb_connection = mariadb.connect(host='your_ip', user='your_user', password='your_pw', database='your_pw')
cursor = mariadb_connection.cursor()

# Retrieve information from database
some_name = 'Seppo Valimaki'
cursor.execute("select name,address from your_table where name=%s", (some_name,))

for name, price in cursor:
	print("Name: {}, Address: {}").format(name,address)

# Insert a new row to a table
try:
	cursor.execute("insert into your_table (name,address) values (%s,%s)", ('Antero Vipunen','334455'))
except mariadb.Error as error:
	print("Error: {}".format(error))

# Commit changes to table, autocommit is disabled by default
mariadb_connection.commit()
print ("The last inseted id was: "), cursor.lastrowid

# Close connection to MariaDb
mariadb_connection.close()
