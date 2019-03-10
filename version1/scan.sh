# Find devices connetted
# fill your own network address and mask
nmap -sn -n -oN scan.txt 111.222.333.444/mask &&

# remove everything but MAC addresses and change : to _
grep -E -o '[[:xdigit:]]{2}(:[[:xdigit:]]{2}){5}' scan.txt > present.txt &&
cat present.txt | sed s/:/_/ | sed s/:/_/ | sed s/:/_/ | sed s/:/_/ | sed s/:/_/ > present.txt

# run v1.py to determine who is missing from work
python v1.py
