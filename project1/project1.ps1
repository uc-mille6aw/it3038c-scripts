#Ask the user for the drive letter of the driver we will be searching. 
$userInput = Read-Host -Prompt 'Enter the drive letter for tyhe drive you would like to search'

# this command searches the drive the user specified for .mp4 files that re larger than 50000000 bytes, or 50 MB. The output is displayed as a table and then sent out to a text file in the same directory that the script is in.

Get-ChildItem ${userInput}:\ -recurse -include *.mp4 -EA SilentlyContinue | where-object {$_.length -gt 50000000} | Sort-Object fullname | format-table fullname, length, LastAccessTime -auto | out-file .\large_videos.txt

#this pause is for troubleshootin and to let the user know when the command has finsished searching. 

PAUSE

#NOTE: I am excluding errors from the Get-ChildItem command (-EA SilentleyContinue) due to the errors I was getting when the command attempted to search windows system file locations. This is unlikely to affect the output since we are only looking for mp4 files.