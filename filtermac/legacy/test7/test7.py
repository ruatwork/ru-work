#!/usr/bin/python3


# reading the first file and setting it as "v"

with open('osoitteet.txt', 'r') as fp:
	v = fp.read()

# reading the second file and setting it as "z"

with open('wanted.txt', 'r') as dp:
        z = dp.read()

# do something if "v" is found in the file "z"

if z in v:
	print ("Gotem")
