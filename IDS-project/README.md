# CodeAlpha: Network Intrusion Detection & Prevention System (NIDS/IPS) 🛡️

## 📝 Project Overview
This project is part of the **CodeAlpha Cyber Security Internship**. It demonstrates a step-by-step implementation of a Network Intrusion Detection System (NIDS) using **Snort 3**, followed by the development of an automated Intrusion Prevention System (IPS) using a custom **Python script** and `iptables`.

## ⚙️ Step-by-Step Implementation & Demonstration

### Step 1: Environment Setup & Interface Identification
First, Snort was installed and the version was verified. Then, the network interfaces were checked to ensure Snort listens on the correct interface (`eth0`).

**Checking Snort Version:**
![Snort Version](screenshots/1.snort-v.png)

**Checking IP Address:**
![IP Address](screenshots/2.ipa.png)

**Identifying Network Interface:**
![Snort Interface](screenshots/3.snort-eth0.png)

### Step 2: Rule Configuration
A custom rule was created in `local.rules` to detect ICMP (Ping) traffic, and the Snort configuration was validated.

**Custom Rule Configuration:**
![Local Rules](screenshots/4.local.rules.png)

**Configuration Validation:**
![Config Check](screenshots/5.config.png)

### Step 3: Initial Testing (Localhost)
To verify the NIDS is working, a test ping was initiated from the Kali machine. Snort successfully detected the traffic.

**Test Ping Executed:**
![Ping Execution](screenshots/6.ping.png)

**Ping Successfully Detected by Snort:**
![Ping Detection](screenshots/7.ping-detected.png)

### Step 4: Automating the Response (IPS Script)
To upgrade the system from NIDS (Detection) to IPS (Prevention), a Python script was developed. Snort was configured to output alerts directly to a log file (`alert.txt`), which the script actively monitors.

**Python IPS Script Creation:**
![Python Script Part 1](screenshots/8.script1.png)
![Python Script Part 2](screenshots/9.script2.png)

**Snort Logging Output:**
![Alert Log](screenshots/10.alert.txt.png)

### Step 5: Live Attack Simulation (Windows XP)
The script was activated, and a live attack was simulated using a separate Windows XP machine to prove the concept in a realistic environment.

**Activating the IPS Script:**
![Activate Script](screenshots/11.activate-script.png)

**Identifying Attacker's IP (Windows XP):**
![Windows XP IP](screenshots/12.ip-xp.png)

**Attacker Initiates Ping Sweep:**
![XP Ping Execution](screenshots/13.ping-xp.png)

### Step 6: Detection, Blocking, and Neutralization
The system detected the incoming attack from the Windows XP machine. The Python script immediately parsed the log, identified the malicious IP, and dynamically blocked it via the firewall.

**Attack Detected:**
![XP Ping Detected](screenshots/14.ping-detected-xp.png)

**IP Automatically Blocked by Script:**
![Block Execution](screenshots/15.block-xp.png)

**Connection Dropped (Attack Neutralized):**
The attacker's terminal immediately shows a "Request timed out" message, confirming the packets are successfully dropped by the Linux firewall.
![Ping Dropped](screenshots/16.drop-ping.png)

---

## 📂 Repository Contents
- `local.rules`: The custom rules configuration file for Snort.
- `response.py`: The Python script responsible for log parsing and automated IP blocking.
- `screenshots/`: Directory containing all execution and demonstration screenshots.

## 🛠️ Tools & Technologies Used
- Linux (Kali) & Windows XP
- Snort 3 (NIDS)
- Python 3 (Automation)
- iptables (Firewall)
