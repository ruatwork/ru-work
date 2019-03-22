#!/bin/python3

# Writes new line to table anyways. Needs to only write if the value of present differs.

# currently running this program prints checklist items one by one with their respective placement in the list

#WHAT WILL THIS DO:

# compare checklist MAC addresses to the currently connected present.txt, then send data to database accordingly


import mysql.connector
from mysql.connector import Error

lastrow = (len(list(open("checklist.txt")))) #get the number of rows in checklist.txt
currentrow = 0 #start from first row

with open("checklist.txt", "r") as checktext: # make checklist.txt into list
	checklist = [item.strip()
		for item in checktext]

with open("present.txt", "r") as presenttext:
	presentlist = [item.strip()
		for item in presenttext]


conn = mysql.connector.connect(host='localhost',
database='timestamp',
user='admin',
password='passu')

# the following will be using the list made from checklist.txt. list name is checklist. there are no real "rows",
# but the variable currentrow is used to go through the list items one by one.

while (currentrow <= lastrow -1): #while we're not past the last row

	try:
		sql_read = "SELECT present FROM " + checklist[currentrow] + " ORDER BY id DESC LIMIT 1"
		cursor = conn.cursor(buffered=True)
		cursor.execute(sql_read)
		record, = cursor.fetchone()

	except Error as e :
		print ("Error while connecting to MySQL", e)

	if checklist[currentrow] in presentlist and (record is 0):
		print (currentrow)
		print (checklist[currentrow]) #print the item from the list that is in the current position (0,1,2,3,4)
		print ("present")

		sql_present = "INSERT INTO " + checklist[currentrow] + " (present) VALUES (1)"

		try:
			cursor.execute(sql_present)
		except Error as e :
			print("Error: {}".format(error))
		conn.commit()

		currentrow += 1 #proceed to next row
		print (sql_present)
		continue

	elif checklist[currentrow] not in  presentlist and (record is 1):
		print (currentrow)
		print (checklist[currentrow])
		print ("absent")

		sql_absent = "INSERT INTO " + checklist[currentrow] + " (present) VALUES (0)"

		try:
			cursor.execute(sql_absent)
		except Error as e :
			print("Error:{}".format(error))
		conn.commit()

		currentrow += 1
		print (sql_absent)
		continue

	elif checklist[currentrow] not in presentlist and (record is 0) or checklist[currentrow] in presentlist and (record is 1):
		print ("not writing")
		currentrow += 1
		continue

	else:
		print("ERROR!! I am the brake :D")
		cursor.close()
		conn.close()
		currentrow += 1
		continue
cursor.close()
conn.close()

# while we're not past the last row:
	# check if currentrow's item is in present.txt
		# if it is, and the last entry in the database is not "present"
			# write to the database that the MAC is present. MAC, present, datetime
			# move to next currentrow

	# else if however currentrow's item is NOT in present.txt
		# and database's last entry is not "absent"
			# write to the database that the MAC is absent. MAC, absent, datetime
# move to next currentrow
