#!/bin/python3

# Writes new line to table anyways. Needs to only write if the value of present differs.

# currently running this program prints checklist items one by one with their respective placement in the list

#WHAT WILL THIS DO:

# compare checklist MAC addresses to the currently connected present.txt, then send data to database accordingly

## Open connection to MariaDB database
import mysql.connector
from mysql.connector import Error

lastrow = (len(list(open("checklist.txt")))) #get the number of rows in checklist.txt
currentrow = 0 #start from first row

## Make a list from the scan results and the file containing known MAC-addresses
with open("checklist.txt", "r") as checktext: # make checklist.txt into list
	checklist = [item.strip()
		for item in checktext]

with open("present.txt", "r") as presenttext:
	presentlist = [item.strip()
		for item in presenttext]

## Log in to MariaDB database
conn = mysql.connector.connect(host='localhost',
database='pilotti',
user='admin',
password='passu')

# the following will be using the list made from checklist.txt. list name is checklist. there are no real "rows",
# but the variable currentrow is used to go through the list items one by one.

while (currentrow <= lastrow -1): #while we're not past the last row

	try:
		sql_read = "SELECT present FROM " + checklist[currentrow] + " ORDER BY id DESC LIMIT 1" # get current item
		cursor = conn.cursor(buffered=True)
		cursor.execute(sql_read)
		record, = cursor.fetchone() # Only fetch one result, notice the use of ","

	except Error as e :
		print ("Error while connecting to MySQL", e)


## Check if MAC-address is found in present list and its record in database is 0, if true, write 1 in the present column in the database, to change status to present
	if checklist[currentrow] in presentlist and (record is 'absent for'):
		print (currentrow)
		print (checklist[currentrow])
		print ("present")

		sql_present = "INSERT INTO " + checklist[currentrow] + " (present) VALUES (present for)" #is present

		try:
			cursor.execute(sql_present)
		except Error as e :
			print("Error: {}".format(error))
		conn.commit() # commit the mariadb writing

		currentrow += 1 #proceed to next row
		print (sql_present)
		continue # start the loop from the start with a new "currentrow"
		
## Check if MAC-address is not in present list and its database record is 1, if true, then write 0 in the present column in the database, to change status to absent
	elif checklist[currentrow] not in  presentlist and (record is "present for"):
		print (currentrow)
		print (checklist[currentrow])
		print ("absent")

		sql_absent = "INSERT INTO " + checklist[currentrow] + " (present) VALUES (absent for)"

		try:
			cursor.execute(sql_absent)
		except Error as e :
			print("Error:{}".format(error))
		conn.commit()

		currentrow += 1
		print (sql_absent)
		continue
		
## If  MAC is found in present list and its record is 1  or it is not found and its record is 0 do nothing :)))
	elif checklist[currentrow] not in presentlist and (record is "absent for") or checklist[currentrow] in presentlist and (record is "present for"):
		print ("not writing")
		currentrow += 1
		continue

## IF somethings not working properly
	else:
		print("ERROR!! I am the brake :D")
		cursor.close()
		conn.close()
		currentrow += 1
		continue

## Close MariaDB connection
cursor.close()
conn.close()
