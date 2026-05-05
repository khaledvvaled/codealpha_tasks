from scapy.all import sniff, IP, TCP, UDP, Raw

def get_protocol_name(proto):
    if proto == 6:
        return "TCP"
    elif proto == 17:
        return "UDP"
    elif proto == 1:
        return "ICMP"
    else:
        return str(proto)

def process_packet(packet):
    if packet.haslayer(IP):
        ip = packet[IP]
        
        print(f"Source: {ip.src}")
        print(f"Destination: {ip.dst}")
        print(f"Protocol: {get_protocol_name(ip.proto)}")
        
        if packet.haslayer(Raw):
            print(f"Payload: {packet[Raw].load}")
        
        print("=" * 50)

sniff(prn=process_packet, store=False)