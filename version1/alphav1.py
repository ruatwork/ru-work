#!/usr/bin/python3

# getting the adresses from a preset text file

with open('checklist2.txt', 'r') as x:
        macs = [item.strip()
                for item in x]

# scan results to a variable

with open('mac2.txt', 'r') as z:
	scan = [item.strip()
		for item in z]

# do something if mac is found in scan

if macs in scan:
	print ("MAC found")

# checking if the variables work

print (macs)

print (scan)
