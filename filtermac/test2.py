#v2

#Does nothing currently

mac = "kissa"

mad = "koira"

sad = "omena"

filu = open("mac.txt", "r")

if filu.mode == 'r':

        filu = filu.read()

if "mac" in "mac.txt":
        print 'gotem'

if "mad" in "mac.txt":
        print 'gotem again'

if "sad" in "mac.txt":
        print 'gotem once more'

