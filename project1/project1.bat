@ECHO OFF
REM This command launches powershell, bypasses the execution policy setting that prevents scripts from running, and runs powershell as an admin. 
REM It uses the special function %~dpn0.ps1 to find ps1 files in the same direcotry as the .bat file.
PowerShell.exe -Command "& {Start-Process PowerShell.exe '-ExecutionPolicy Bypass -File ""%~dpn0.ps1""' -Verb RunAS}"
PAUSE