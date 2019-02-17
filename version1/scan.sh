# Find devices connetted
# fill your own network address and mask
nmap -sP -n -oN scan.txt 111.222.333.444/mask &&

# remove everything but MAC addresses
grep -E -o '[[:xdigit:]]{2}(:[[:xdigit:]]{2}){5}' scan.txt > present.txt &&

# run v1.py to determine who is missing from work
python v1.py
