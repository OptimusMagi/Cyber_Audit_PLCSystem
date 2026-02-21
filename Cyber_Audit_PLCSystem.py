#TODO: Cybersecurity Audit for a PLC System
# What it does: Simulate a vulnerability scan on a PLC system using Python.
# Steps:
# 1. Use a Python script to simulate checking for common vulnerabilities (like open ports, outdated firmware).
# 2. Report the findings in a simple format.

#TODO: Code script for vulnerability scanning:
import socket

def check_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((host, port))
    s.close()
    return result == 0

# Check common ports
target = "localhost"
ports = [502, 445, 135, 443]

print(f"Checking {target} for open ports...")
for port in ports:
    if check_port(target, port):
        print(f"Port {port} is OPEN! This could be a security risk.")
    else:
        print(f"Port {port} is closed.")

# Explanation:
# This is like checking if doors in a building are unlocked.
# If they’re open, it means someone might get in without permission

# Into details:
# This project simulates checking a PLC system for security holes. It looks for open ports that could allow hackers to access the system.
# This is part of ensuring the safety of industrial control systems.