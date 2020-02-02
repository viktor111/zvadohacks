import scapy.all as scapy
import optparse
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=processPacket)

def processPacket(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw]
            print(load)

sniff("enp3s0")
