"""Simple TCP port scanner (learning exercise).

Only scan machines you own or have written permission to test.

Examples:
    python3 port_scanner.py 127.0.0.1
    python3 port_scanner.py 192.168.56.101 -s 1 -e 1024
"""
import argparse
import ipaddress
import socket


def is_open(host, port, timeout=0.5):
    """Return True if a TCP connection to host:port succeeds."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        return s.connect_ex((host, port)) == 0


def is_local_or_private(host):
    """True for localhost and private network addresses."""
    ip = ipaddress.ip_address(socket.gethostbyname(host))
    return ip.is_loopback or ip.is_private


def main():
    parser = argparse.ArgumentParser(description="Simple TCP port scanner")
    parser.add_argument("host", help="target host or IP")
    parser.add_argument("-s", "--start", type=int, default=1, help="first port")
    parser.add_argument("-e", "--end", type=int, default=1024, help="last port")
    args = parser.parse_args()

    if not (1 <= args.start <= args.end <= 65535):
        parser.error("ports must satisfy 1 <= start <= end <= 65535")

    if not is_local_or_private(args.host):
        answer = input("This is not a local/private address. "
                       "Do you own it or have written permission? (yes/no): ")
        if answer.strip().lower() != "yes":
            print("Stopped.")
            return

    print(f"Scanning {args.host} ports {args.start}-{args.end} ...")
    found = [p for p in range(args.start, args.end + 1) if is_open(args.host, p)]

    if found:
        for p in found:
            print(f"Port {p} is OPEN")
    else:
        print("No open ports found in this range.")
    print("Scan complete.")


if __name__ == "__main__":
    main()
