#!/usr/bin/python3

# checks external text files and makes them into lists

# TODO compare these lists to determine who is at work and who is not

with open("checklist.txt", "r") as alltext:
	checklist = [item.strip()
		for item in alltext]

with open("mac2.txt", "r") as crontext:
	paikalla = [item.strip()
		for item in crontext]

print checklist
print paikalla
