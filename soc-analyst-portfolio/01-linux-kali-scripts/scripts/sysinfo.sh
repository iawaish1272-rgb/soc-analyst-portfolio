#!/bin/bash
# Prints basic system information (learning exercise).
# Run: chmod +x sysinfo.sh && ./sysinfo.sh

echo "===== System Information ====="
echo "Hostname:     $(hostname)"
echo "User:         $(whoami)"
echo "Date:         $(date)"
echo "Kernel:       $(uname -r)"
echo "IP address:   $(hostname -I)"
echo "Disk usage:   $(df -h / | awk 'NR==2 {print $3 " used of " $2}')"
echo "=============================="
