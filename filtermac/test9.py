#!/usr/bin/python3

# testing out the if something in a file do something

# this variable would be the mac

muuttuja = "koira"

muuttujaa = "omena"

muuttujab = "jotain"

olematon = "kissa"

# reading the file

with open('mac.txt', 'r') as fp:
	v = fp.read()

# do something if variable is found in the file

if muuttuja in v:
	print ("Gotem")

if muuttujaa in v:
        print ("Gotem again")

if muuttuja and muuttujaa in v:
	print ("Both found")

if muuttuja and muuttujaa and muuttujab in v:
	print ("All 3 found in the file")

if olematon not in v:
	print ("Ei ole kissaa")
