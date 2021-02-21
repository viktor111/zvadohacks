import pyfiglet
import subprocess


banner = pyfiglet.figlet_format("zvadohacks console")
print(banner)

def mac_change(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    print("[+] shutdown interface")
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    print("[+] changing MAC address")
    subprocess.call(["ifconfig", interface, "up"])
    print("[+] interface up MAC changed")

def read_command():
    command = input("-> ")
    if "help" in command:
        print("help messege")
        return
    if "run" in command:
        list_command = command.split()
        print(list_command)
        if len (list_command) < 1:
            print("[-] Please input a tool to run")
            read_command()
        elif len(list_command) > 1:
            if list_command[1] == "macchange":
                try:
                    interface = list_command[2]
                    new_mac = list_command[3]
                except:
                    print("[-] Input interface and mac address")
                    read_command()
                mac_change(interface, new_mac)


while True:
    read_command()
