## README
		
1. Install requirements

		sudo apt-get install nmap python

- Be cautious when using nmap, check the ip multiple times to be sure of it.
- Only scan networks you know you have permission to scan.
- RU@work is not liable for any illegal or wrong use of nmap.
- This program does not scan open ports.

2. Edit checklist.txt with all the MAC addresses you wish to track, each address in its own row.

3. Make the script executable

		chmod +x scan.sh
		

Run the programs with

		bash scan.sh


### OPTIONAL:

If you wish to automate the program to run in set intervals, use cron.

4. Edit your cron-file to run the script and the program
		
		sudo crontab -e

Copy and paste the settings found in cron.txt
