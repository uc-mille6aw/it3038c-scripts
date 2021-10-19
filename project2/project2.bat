@ECHO OFF
REM This command launches powershell, bypasses the execution policy setting that prevents scripts from running, and runs powershell as an admin. 
REM This batch file is an updated version of the project 1 version that reduces complexity and eliminates the unnecessary pause.
PowerShell.exe -Command "& {Start-Process PowerShell.exe '-ExecutionPolicy Bypass -File ""project2.ps1""' -Verb RunAS}"
