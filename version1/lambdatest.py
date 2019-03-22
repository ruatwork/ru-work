#!/bin/python3

lastrow = (len(list(open("checklist.txt"))))
currentrow = 0
with open("checklist.txt", "r") as checktext:
	checklist = [item.strip()
		for item in checktext]


with open("present.txt", "r") as presenttext:
	presentlist = [item.strip()
		for item in presenttext]


if any(map(lambda each: each in checklist[currentrow], presentlist)):
	print (currentrow)
	print (checklist[currentrow]) #print the item from the list that is in the current position (0,1,2,3,4)
	print ("present")
