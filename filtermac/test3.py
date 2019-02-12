#!/usr/bin/python3

# testing out the if something in a file do something

import codecs

# this variable would be the mac

muuttuja = 'koira'

# reading the file

with open('mac.txt', 'rb') as fp:
	v = fp.read()

# do something if variable is found in the file

print (v)

if 'muuttuja' in 'v':
	print ('muuttuja')
