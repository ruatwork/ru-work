## Salt states for the project

Currently in the making, some of them are usable and tested. The one for rasp-pi shouldn't be a problem since the main thing is the connection through NAT anyways.

Worked on with a vagrant machine with Ubuntu 16.04.5 LTS on it.

### Todo

The state for mariadb (should work like mysql).

Make sure pip.installed works on the server.

Merge the website with all the pictures and stuff when ready into github.

Finish all the little stuff and try it out with a GUI.

Test on an actual fresh installation with the same OS that our server is going to use.

Maybe an installation script just to be fancy ?

### Notes

Remember ports 4505 and 4506 tcp on master.

Some of the states have "user" in them, make sure to switch them for the actual username when put in actual use.
