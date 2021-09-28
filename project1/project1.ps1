#Ask the user for the drive letter of the drive we will be searching. 
$userInput = Read-Host -Prompt 'Enter the drive letter for the drive you would like to search'

#These 2 lines save the current working directory location of the scripts to the variable $dir. Without this, the out-file output will not go where the user can easily find it.
$scriptpath = $MyInvocation.MyCommand.Path
$dir = Split-Path $scriptpath

# this command searches the drive the user specified for .mp4 files that are larger than 50000000 bytes, or 50 MB. The output is displayed as a table and then converted to a string (for formating reasons) Lastly, the output is sent to a text file in the same directory that the script is in.

Get-ChildItem ${userInput}:\ -recurse -include *.mp4 -EA SilentlyContinue | where-object {$_.length -gt 50000000} | Sort-Object fullname | format-table fullname, length, LastAccessTime -AutoSize | out-string -width 10000 | out-file $dir\large_videos.txt

#this pause is for troubleshooting and to let the user know when the command has finished searching. 

PAUSE

#NOTE: I am excluding errors from the Get-ChildItem command (-EA SilentleyContinue) due to the errors I was getting when the command attempted to search windows system file locations. This is unlikely to affect the output since we are only looking for mp4 files.
