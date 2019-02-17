#!/bin/bash

# activate nmap to find devices connected to your network
sudo nmap -sP -n -oN /tmp/scan.txt 192.xxx.xxx.xxx/xx &&

# take the MAC addresses and output them into presents.txt
grep -E -o '[[:xdigit:]]{2}(:[[:xdigit:]]{2}){5}' /tmp/scan.txt > /tmp/present.txt &&

# run v1.py, which will compare the addresses on the files.
# remember to insert the known MAC addresses to checklist.txt
python v1.py
