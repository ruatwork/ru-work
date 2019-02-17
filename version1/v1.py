#!/usr/bin/python3

# checks external text files and makes them into lists


# open and make a list of the file containing the MAC addresses of all employees
with open("/tmp/checklist.txt", "r") as alltext:
	checklist = [item.strip()
		for item in alltext]

# open and make a list of the file containing current connected MAC addresses
with open("/tmp/present.txt", "r") as nmaptext:
	present = [item.strip()
		for item in nmaptext]

print (checklist)
print (present)

# compare checklist and present list - those in present are at work, those missing are not

absent = set(checklist) - set(present)

with open('/tmp/absent.txt', 'w') as abstext:
	for i in absent:
		abstext.write("%s\n" % i)
		print(i)
#print (set(checklist) - set(present))
