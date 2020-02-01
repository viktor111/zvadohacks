import scapy.all as scapy

packet = scapy.ARP(op=2, pdst="192.168.0.101", hwdst="00:23:d1:d0:cd:21", psrc="192.168.0.1")
