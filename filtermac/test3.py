#!/usr/bin/python3

# testing out the if something in a file do something

import codecs

# this variable would be the mac

muuttuja = 'kissa'

# reading the file

with open('mac.txt', 'rb') as fp:
	v = fp.read()

# do something if variable is found in the file

if 'muuttuja' in 'v':
	print (gotem)
