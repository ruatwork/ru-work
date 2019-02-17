#!/usr/bin/python3

# testing out the if something in a file do something

# this variable would be the mac

muuttuja = "koira"

muuttujaa = "omena"

# reading the file

with open('mac.txt', 'r') as fp:
	v = fp.read()

# do something if variable is found in the file

if muuttuja in v:
	print ("Gotem")

if muuttujaa in v:
        print ("Gotem again")

