#v2

#Does nothing currently

mas = "kissa"

mad = "koira"

sad = "omena"

filu = open("mac.txt", "r")

if filu.mode == 'r':

        filu = filu.read()
	print(filu)

if "mas" in "filu":
        print 'gotem'

if "sad" in "mac.txt":
        print 'gotem once more'

print "Hello world!"
