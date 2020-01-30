import subprocess
import optparse

def getArgs():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Specify interface to change MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="Input new mac address")
    return parser.parse_args()

def changeMac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    print("[+] shutdown interface")
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    print("[+] changing MAC address")
    subprocess.call(["ifconfig", interface, "up"])
    print("[+] interface up MAC changed")

(opt, args) = getArgs()

changeMac(opt.interface, opt.new_mac)
