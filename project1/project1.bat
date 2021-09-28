@ECHO OFF
PowerShell.exe -Command "& {Start-Process PowerShell.exe '-ExecutionPolicy Bypass -File ""%~dpn0.ps1""' -Verb RunAS}"
PAUSE