# TODO

## First program needed

### Steps:
DONE 1. Nmap prints the MAC addresses found on the network  
DONE 2. Use grep to make a clean list of the MAC addresses  
3. if a MAC address is missing from the list, print something ("No")

### Another program?
Somehow the program needs to know when the users status changes from "connected" to "not connected" and marking it just once into the actual time managent database.

## Second program needed

### Steps:
1. Acquiring addresses from an external text file
2. Nmap's scan done every 1-5min in cron


## Third program needed

### Steps:
1. Program needs to send data of MAC addresses/real names to a VPS with MariaDB
2. Data needs to include: date, identifier, in/out/(not) at work, optionally work time

#### problems:
The program must send the data in a format MariaDB will be able to understand. Python libaries?

## Fourth program needed

### Steps:
1. Web interface for the end users to log in/log out in case they do not wish to use automatic WiFi logging
2. Web interface to view the logged work time of the user
3. Web interface to fix incorrect work time data
