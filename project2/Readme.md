# Project 2

### Overview
<p> 
This is my script for project 2. The idea for this script was to convert the current time into a different timezone. 
This is useful if you want to know what time it is in various places around the world.
This script only works with windows systems and requires admin access.
</p>

### How to run the script
<p>
To run the script, download my 'project2.bat' and 'project2.ps1' files. Place these files into a folder by themselves (they should be the only files in the folder). 
Double click the project2.bat file to open it and begin.
</p>

### Using the script
<p>
The script will begin with listing all of the times zones that windows/powershell is aware of. The script will then ask you to enter a time zone to convert the current time into. 
If you enter a time zone that my script does not recognize, it will give you a chance to try again.
Once a recognizable time zone is entered, the script will convert the current date and time into that time zone's date and time.
</p>

### Interpreting the output
<p>
The output will be in mm/dd/yyyy hh:mm:ss AM/PM format. Once you are ready to close the window, hit enter.
</p>

### Misc Info
<p>
This script is a different script than my project 1 script. This time around I wanted to make a script that incorportated error handling (try, catch) and a loop. 
I also updated my script launcher (the .bat file) to improve things/avoid issues and remove the unnecessary pause.
</p>
