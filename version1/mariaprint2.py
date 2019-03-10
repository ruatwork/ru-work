import mysql.connector
from mysql.connector import Error
try:
	conn = mysql.connector.connect(host='localhost',
					database='test',
					user='admin',
					password='Work@Hom3')
	sql_Query = "SELECT present FROM test ORDER BY id DESC LIMIT 1"
	cursor = conn.cursor(buffered=True)
	cursor.execute(sql_Query)
	record = cursor.fetchone()
	print ("Printing first record using cursor.fetchone()", record)
	cursor.close()
except Error as e :
	print ("Error while connecting to MySQL", e)
finally:
	#closing database connection.
	if(conn.is_connected()):
		conn.close()
		print("connection is closed")
