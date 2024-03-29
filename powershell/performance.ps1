﻿$Machines = 'localhost' 

Foreach ($machine in $Machines)  

{ 

$pt = (Get-Counter -Counter "\Processor(_Total)\% Processor Time" -SampleInterval 1 -MaxSamples 3).CounterSamples.CookedValue 

    $sample = 1 

    foreach ($p in $pt) { 

        $DATE = Get-Date -Format g

        "[3] - Sample {2}: CPU is at {0}% on {1}" -f [int]$p, $machine, $sample, $date | out-file -append C:\output.txt 

        $sample++ 

    } 

} 
