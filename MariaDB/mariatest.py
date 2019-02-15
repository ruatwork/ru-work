# This works locally

#!/usr/bin/python
import mysql.connector as mariadb

# Connect to MariaDB
mariadb_connection = mariadb.connect(user='tesi', password='1testi2', database='testi')
cursor = mariadb_connection.cursor()

# Retrieve information from database
some_name = 'Banaani'
cursor.execute("select name,price from test1 where name=%s", (some_name,))

for name, price in cursor:
	print("Name: {}, Price: {}").format(name,price)

# Insert a new row to a table
try:
	cursor.execute("insert into test1 (name,price) values (%s,%s)", ('Ateria','103.4'))
except mariadb.Error as error:
	print("Error: {}".format(error))

# Commit changes to table, autocommit is disabled by default
mariadb_connection.commit()
print ("The last inseted id was: "), cursor.lastrowid

# Close connection to MariaDb
mariadb_connection.close()
