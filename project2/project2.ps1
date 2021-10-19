#This lists the various time zones that windows/powershell is aware of, and filters for only the name/ID property
[System.TimeZoneInfo]::GetSystemTimeZones() | Select-Object -Property Id | Out-Host

#this loop will continue until the user provides a correct time zone name
do{
    $fail=$false
    try{
        #this asks the user to enter a time zone to convert the current time to
        $userInput = Read-Host -Prompt "Enter the name of one of the time zones above to convert the current time to that time zone"
        #this convers the tcurrent time to the time zone that the user entered
        $date = [System.TimeZoneInfo]::ConvertTimeBySystemTimeZoneId((Get-Date), "$userInput")
            #this outputs the converted time/date and exits the loop
           Write-Host $date
           break

        }
    #this catches the error that occurs when an unknown/misspelled time zone is entered and gives the user a another chance to try again
    catch [TimeZoneNotFoundException]{

        Write-Host "I do not know that time zone, try again"}
        $fail=$true
 } while ($fail)
 #this simply prevents the window from closing before the user has time to see the output
 Read-Host -Prompt "Press Enter to close this window and stop the script"