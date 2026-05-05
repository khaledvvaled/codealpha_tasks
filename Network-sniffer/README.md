# CodeAlpha: Basic Network Sniffer 🕵️‍♂️

## 📝 Project Overview
This project is part of the **CodeAlpha Cyber Security Internship**. The goal was to build a functional **Network Sniffer** using Python and the `scapy` library to capture and analyze network traffic in real-time.

The sniffer is designed to identify source and destination IP addresses, protocols (TCP, UDP, ICMP), and extract sensitive information from the data payload, such as login credentials from unencrypted HTTP traffic.

## 🚀 Features
- **Real-time Packet Capture:** Monitors network interfaces for incoming and outgoing traffic.
- **Protocol Identification:** Automatically identifies and labels common network protocols.
- **Payload Extraction:** Extracts and displays raw data from packets to analyze content.
- **Credential Interception:** Successfully demonstrates the ability to capture plain-text usernames and passwords from vulnerable web applications.

## 📸 Demonstration & Screenshots

### 1. The Vulnerable Target
For testing purposes, I used a deliberately vulnerable web application to simulate a real-world scenario where data is sent without encryption.
![Target Website](screenshorts/test.png)

### 2. The Sniffer Script
The core logic of the sniffer was developed using Python's `scapy` library, focusing on filtering IP layers and extracting raw data.
![Python Script](screenshorts/script.png)

### 3. Successful Data Capture (POC)
The sniffer successfully captured a **POST request**, revealing the captured **username and password** in clear text within the payload.
![Data Captured](screenshorts/sniff.png)

## 🛠️ Tools & Technologies Used
- **Python 3**
- **Scapy Library**