#!/bin/sh

# Check if Python is installed on the system
$pythonInstalled = $null
try {
    $pythonInstalled = Get-Command python -ErrorAction Stop
} catch {
    # Python is not installed
    ## do stuff here
}

# setting the working directory
cd C:\Users\NilanBais\Documents\Github\cream-invoice-machine