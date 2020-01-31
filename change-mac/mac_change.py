import subprocess
import optparse
import re

def getArgs():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Specify interface to change MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="Input new mac address")
    (opt, arg) = parser.parse_args()
    if not opt.interface:
        parser.error("[-] Please specify an interface. Use --help for information.")
    elif not opt.new_mac:
        parser.error("[-] Please specify a new mac address. Use --help for information.")
    return opt

def changeMac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    print("[+] shutdown interface")
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    print("[+] changing MAC address")
    subprocess.call(["ifconfig", interface, "up"])
    print("[+] interface up MAC changed")

opt = getArgs()
changeMac(opt.interface, opt.new_mac)

def ifconfig():
    ifconfigResult = subprocess.check_output(["ifconfig", opt.interface])
    print(ifconfigResult)
    return ifconfigResult

macSearchResult = re.search(rb"\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig())

if not macSearchResult:
    print("[-] could not read MAC address. Use --help for more info")
