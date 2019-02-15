#!/usr/bin/python3

# TEST LOOP

# testing out the if something in a file do something

# this variable would be the mac

#muuttuja = "11AA"

#muuttujaa = "33CC"

#muuttujab = "55EE"

#olematon = "77GG"

checklist = ['11AA','33CC','55EE','77GG']

# reading the file

with open('mac2.txt', 'r') as cronlist:
	list2 = []
	for item in cronlist:
		number  = 0
		while number < 1:
			list2.append(item)
			number += 1
	print (list2)
#	maclist = cronlist.read()



# do something if variable is found in the file

#if muuttuja in maclist:
#	print ("Gotem")

#if muuttujaa in maclist:
#        print ("Gotem again")

#if muuttuja and muuttujaa in maclist:
#	print ("Both found")

#if muuttuja and muuttujaa and muuttujab in maclist:
#	print ("All 3 found in the file")

#if olematon not in maclist:
#	print ("Ei ole kissaa")

