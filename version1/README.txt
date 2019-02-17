Steps:

	1. Install requirements
		
		sudo apt-get install nmap python

	### Be cautious when using nmap, check the ip multiple times.
	### Only scan networks you know you have permission to scan.
	### This program does not scan open ports.

	2. Move the script and the program into /tmp

		mv scan.sh /tmp
		mv pythonprogram.py /tmp

	3. Make the script executable

		chmod +x /tmp/scan.sh

	4. Edit your cron-file to run the script and the program
		
		sudo crontab -e

		Inside copy and paste the settings found in cron.txt
