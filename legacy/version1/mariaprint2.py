import mysql.connector
from mysql.connector import Error
try:
	conn = mysql.connector.connect(host='localhost',
					database='worktime',
					user='admin',
					password='your_password')
	sql_Query = "SELECT present FROM aa_ff_3r_11_22_33 ORDER BY id DESC LIMIT 1"
	cursor = conn.cursor(buffered=True)
	cursor.execute(sql_Query)
	record = cursor.fetchone()
	print (record)
	cursor.close()
except Error as e :
	print ("Error while connecting to MySQL", e)
finally:
	#closing database connection.
	if(conn.is_connected()):
		conn.close()
		print("connection is closed")
