function getIP{
(Get-NetIPAddress).ipv4address | Select-String "192*"
}

function getAccount{
($env:username)
}

function getHOSTNAME{
($env:COMPUTERNAME)
}

function getVersion{
($Host.version.major)
}

function getDate {
(Get-Date -format "dddd, MM-dd-yyyy")
}

$IP=getIP
$User=getAccount
$HostName=getHOSTNAME
$Version=getVersion
$Date=getDate
Write-Output("This machine's IP is $IP. User is $User. Hostname is $HostName. Powershell Version $Version. Today's date is $Date.") >> C:\it3038c-scripts\powershell\Lab3.txt