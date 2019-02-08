#testing out the if something in a file do something

mac = "kissa"

filu = open("mac.txt", "r")

if filu.mode == 'r':

	filu = filu.read()

if "mac" in "mac.txt":
	print 'gotem'
