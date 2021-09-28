<h1> Andrew Miller - Project 1 Script </h1>
<br>
<p> This script was created for project 1. This script searches a user specified drive letter for any .mp4 files over ~50 MB in size. </p>
<br>
<h3> Running the File: </h3>
<p> To run the file, place both the project1.ps1 and project1.bat files into a folder on your device. They need to be in the same folder for the script to work. No other script files should be there, just the files I specified. Double click the project1.bat file to begin. Note: One of the following windows may ask for admin access. Next, it will ask for the drive letter you would like to scan. The scan will take a few moments to complete. When finished, the script will say something like "Press enter to continue". You will then find a file named "large_videos.txt" in the same folder with the two files you downloaded earlier. Open this file and you will find a list in table format listing all .mp4 files on the drive you specified that are larger than 50MB.</p>
<br>
<h3> Interpreting the Output </h3>
<p> The output should be fairly self explanatory. The "fullname" column states the path and name of the .mp4 file. The "Length" column displays the size of the file in bytes. Finally, the "LastAccessTime" column displays the date and time that the file was last accessed.
<br>
<h3> References:</h3>
<p>I used the following as references for making certain pieces of the script(s).
<br>
For the .ps1 file, I referenced this SumTips.com article on using the Get-ChildItem command: https://sumtips.com/tips-n-tricks/find-files-larger-than-a-specific-size-with-powershell-command-prompt/
<br>
SumTips. (2018, September 6). Retrieved from: https://sumtips.com/tips-n-tricks/find-files-larger-than-a-specific-size-with-powershell-command-prompt/.
<br>
I wanted to make running the .ps1 script easier for the user, so I wanted to launch it via a double click. I accomplished this by following this guide from howtogeek.com: https://www.howtogeek.com/204088/how-to-use-a-batch-file-to-make-powershell-scripts-easier-to-run/
<br>
Zinicola, J. (2017, September 10). How to use a batch file to make powershell scripts easier to run. How to Geek. Retrieved from https://www.howtogeek.com/204088/how-to-use-a-batch-file-to-make-powershell-scripts-easier-to-run/

</p>
