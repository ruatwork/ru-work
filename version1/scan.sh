# install nmap with
# Run with sudo

#Find devices connetted
nmap -sP -n -oN /tmp/scan.txt ip.ad.re.ss/mask

#Grep adresses from scan results
grep -E -o '[[:xdigit:]]{2}(:[[:xdigit:]]{2}){5}' /tmp/scan.txt > /tmp/present.txt
