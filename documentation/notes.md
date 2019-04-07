https://stackoverflow.com/questions/5687718/how-can-i-insert-data-into-a-mysql-database  

###Creating user in MariaDB  
https://mariadb.com/kb/en/library/create-user/  

###Granting privileges to user  
https://mariadb.com/kb/en/library/grant/  
  
### Python integration with MariaDB  
https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/
  
###Reference for Python and MySQL Database(might be useful)  
https://www.youtube.com/watch?v=lhU2OZCKXhQ  
  
https://www.raspberrypi.org/forums/viewtopic.php?t=165213  

### Running cron as root
Just remember to use sudo

## Problems?
- Best way to determine whether you're at work - some calculations in PHP(?) based on last timestamp data?
- data to be sent to mariaDB: MAC address, timestamp, at work or not, possibly employee name?

## Calculations for server usage and resource planning
Our test database was 0.03 MB and had one table with 9 rows.
The program is planned to make 288 scans per day, and if we use the same size average per row it comes out as 1MB per day.
Our current server resources are 1TB of data transfer/month and we've allocated atleast 10GB for the database.
In other words the cheapest vps from DigitalOcean should be more than enough for the project!

### Incrontab

- chmod a+x ../maria.py
- absolute paths to files in maria.py
- <FILE TO WATCH> IN_MODIFY /usr/bin/python3 <PATH TO maria.py>
