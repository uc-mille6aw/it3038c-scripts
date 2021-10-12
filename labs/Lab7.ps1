Import-Module NTFSSecurity

$userPath = Read-Host -prompt "Enter the path where you would like to learn more about security settings"

cd $userPath

Add-Content -path .\NtfsInfo.txt -value "An overview of all permissions:" 

dir | Get-NTFSAccess | format-table -autosize | out-file -append -encoding ascii -FilePath .\NtfsInfo.txt

Add-Content -path .\NtfsInfo.txt -value "A list of owners:"

dir | Get-NTFSOwner | out-file -append -encoding ascii -FilePath .\NtfsInfo.txt

Add-Content -path .\NtfsInfo.txt -value "File permission inheritance information:"

dir | Get-NTFSInheritance | out-file -append -encoding ascii -FilePath .\NtfsInfo.txt