# 01 - Linux, Kali and small scripts

## What I practised
Navigating the file system, file permissions, users and processes, installing tools with apt, and basic networking commands in a Kali VM.

## Commands I use most
| Command | What it does |
|---|---|
| `ls -la` | list files with permissions and hidden files |
| `chmod 755 file` | set permissions with numbers |
| `grep -i "word" file` | search text in a file |
| `ps aux` | show running processes |
| `ss -tuln` | show listening ports |
| `ip a` | show my IP addresses |

TODO: add 3-5 commands that confused you at first, and write how you finally understood them.

## Scripts
- [`scripts/port_scanner.py`](scripts/port_scanner.py) - a simple TCP port scanner.
- [`scripts/sysinfo.sh`](scripts/sysinfo.sh) - prints basic system information.

These started as learning exercises. TODO: write one or two lines about what you changed or improved yourself (for example: a new option, a bug you fixed).

## Safety
The port scanner asks for confirmation before scanning anything that is not a local or private address.
