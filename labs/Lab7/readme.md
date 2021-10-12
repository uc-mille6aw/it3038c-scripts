<h1>Lab 7</h1>

<p>This is my script for lab 7. This script scans a user selected directory and outputs file permissions and security information to a text file.
  To run the script, you will first need to install the module that is being used for this script. The module is called 'NTFSSecurity'.</p>
<h5>Note: This script only works with NTFS file systems</h5>

<h3>Installing the module and running the script</h3>

<p>First, open PowerShell ISE as an admin.
  Next, make sure you have no execution policies in place that prevent scripts from running (set-executionpolicy unrestricted).
  To install the module we will be using, in the PowerShell console, type:</p>
  
  ```powershell
  Install-Module -Name NTFSSecurity
  ```
  <p>
  Accept any prompts to get the install underway. Once the module is installed, you are ready to download, open, and run my script in PowerShell ISE.
  You will be prompted to enter the path to the directory you would like to scan (spelling is important).</p>

<h3>Interpreting Output</h3>

<p>The output for this script will be a file called "NtfsInfo.txt". The file will be saved to the directory you scanned.
  Opening the file will display information pulled from the directory using the NTFSSecurity module including file security information, ownership, and more.
</p>
