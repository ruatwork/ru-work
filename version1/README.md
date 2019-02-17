# README

## What does it do?

This is the first version of RU@work.

Currently RU@work saves the present/missing MAC addresses locally. In the future MariaDB integration will be present with timestamps.

## How do I do it?
		
1. Install requirements

		sudo apt-get install nmap python

- Be cautious when using nmap, check the ip multiple times to be sure of it.
- Only scan networks you know you have permission to scan.
- RU@work is not liable for any illegal or wrong use of this program or nmap.
- This program does not scan open ports.

2. Edit checklist.txt with all the MAC addresses you wish to track, each address in its own row.

3. Make the script executable

		chmod +x scan.sh

Run the program with

		bash scan.sh
		
After running, the MAC addresses that are not connected are saved in absent.txt, while those that are are saved in present.txt.

### OPTIONAL:

If you wish to automate the program to run in set intervals, use cron.

4. Edit your cron-file to run the script and the program
		
		sudo crontab -e

Copy and paste the settings found in cron.txt
