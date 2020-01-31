import scapy.all as scapy

def scan(ip):
    arpRequest = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arpRequestBroadcast = broadcast/arpRequest
    answered, unanswered = scapy.srp(arpRequestBroadcast, timeout=1)
    print(answered.summary())

scan("192.168.0.1/24")

