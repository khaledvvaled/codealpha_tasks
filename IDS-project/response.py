import os
import time
import re

LOG_FILE = "alert.txt"
BLOCKED_IPS = set()

SAFE_IPS = ["127.0.0.1", "192.168.1.38", "8.8.8.8", "192.168.1.1"]

def block_ip(ip_address):
    if ip_address in SAFE_IPS:
        return 
        
    if ip_address not in BLOCKED_IPS:
        print(f"[!] Real attack detected from: {ip_address}. Blocking...")
        os.system(f"sudo iptables -A INPUT -s {ip_address} -j DROP")
        BLOCKED_IPS.add(ip_address)
        print("[+] IP Blocked Successfully by Firewall.")

print(f"[*] Monitoring {LOG_FILE} for real intrusions...")

if not os.path.exists(LOG_FILE):
    open(LOG_FILE, 'w').close()

with open(LOG_FILE, "r") as file:
    file.seek(0, 2)
    
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.5)
            continue
            
        if "Ping Detected" in line:
            match = re.search(r'\}\s+([0-9\.]+)\s+->', line)
            if match:
                attacker_ip = match.group(1)
                block_ip(attacker_ip)
