#!/bin/python3


#checklist.txt, mariadb.py, verrataan present.txt:hen
#
#while currentrow <= lastrow
#     if checklist's MAC is in present (readlines)
#           and if tableLastRow != present
#              write to database (tableName=MAC(readlines),lastTableRowID+1, MAC, present,datetime)
#               currentrow += 1
#     else if checklist's MAC not present (readlines)
#         and if tableLastRow != absent
#             write to database (tableName=MAC(readlines),lastTableRowID+1, MAC, absent,datetime)
#             currentrow += 1




# get the number of rows in file
lastrow = (len(list(open("checklist.txt"))))
print (lastrow)
currentrow = 1 #start from first row
checkmac = 'foo'

while currentrow <= lastrow
	

# is it wiser to make checklist.txt to a python list and use a for list item loop to cycle
# through the items to check whether they're in present.txt,
# or to read checklist.txt and check each line individually?
