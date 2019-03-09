#!/bin/python3

# currently running this program prints checklist items one by one with their respective placement in the list

#WHAT WILL THIS DO:

# compare checklist MAC addresses to the currently connected present.txt, then send data to database accordingly

#while currentrow <= lastrow
#     if checklist's MAC is in present (readlines)
#           and if tableLastRow != present
#              write to database (tableName=MAC(readlines),lastTableRowID+1, MAC, present,datetime)
#               currentrow += 1
#     else if checklist's MAC not present (readlines)
#         and if tableLastRow != absent
#             write to database (tableName=MAC(readlines),lastTableRowID+1, MAC, absent,datetime)
#             currentrow += 1



lastrow = (len(list(open("checklist.txt")))) #get the number of rows in checklist.txt
currentrow = 0 #start from first row
# checkmac = 'foo'

with open("checklist.txt", "r") as checktext: # make checklist.txt into list
	checklist = [item.strip()
		for item in checktext]

# the following will be using the list made from checklist.txt. list name is checklist. there are no real "rows",
# but the variable currentrow is used to go through the list items one by one.

while (currentrow <= lastrow -1): #while we're not past the last row
	print (currentrow)
	print (checklist[currentrow]) #print the item from the list that is in the current position (0,1,2,3,4)
	currentrow += 1 #proceed to next row

#
# while we're not past the last row:
	# check if currentrow's item is in present.txt
		# if it is, and the last entry in the database is not "present"
			# write to the database that the MAC is present. MAC, present, datetime
			# move to next currentrow

	# if however currentrow's item is NOT in present.txt
		# and database's last entry is not "absent"
			# write to the database that the MAC is absent. MAC, absent, datetime
			# move to next currentrow
