#!/usr/bin/python3

# checks external text files and makes them into lists


# open and make a list of the file containing the MAC addresses of all employees
with open("checklist.txt", "r") as alltext:
	checklist = [item.strip()
		for item in alltext]

# open and make a list of the file containing current connected MAC addresses
with open("present.txt", "r") as nmaptext:
	present = [item.strip()
		for item in nmaptext]

print ('Known MAC addresses: ' + str(checklist))
print ('MAC addresses at work: ' + str(present))

# compare checklist and present list - those in present are at work, those missing are not

absent = set(checklist) - set(present)

# export missing MAC addresses to absent.txt
with open('absent.txt', 'w') as abstext:
	for i in absent:
		abstext.write("%s\n" % i)
		print('NOT at work: ' + str(i))
