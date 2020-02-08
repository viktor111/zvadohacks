import scapy.all as scapy
import optparse
from mac_vendor_lookup import MacLookup

def getArgs():
    parser= optparse.OptionParser()
    parser.add_option("-i", "--ip", dest="ip", help="Input IP address using -i or --ip.")
    (opt, arg) = parser.parse_args()
    return opt

def scan(ip):
    arpRequest = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arpRequestBroadcast = broadcast/arpRequest
    answered = scapy.srp(arpRequestBroadcast, timeout=1, verbose=False)[0]

    print("IP\t\t\tMAC Address\t\t\tVendor\n-----------------------------------------------------------")
    for el in answered:
        print(el[1].psrc + "\t\t" + el[1].hwsrc + "\t\t" + MacLookup().lookup(el[1].hwsrc))

opt = getArgs()
scan(opt.ip)

