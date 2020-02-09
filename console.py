import pyfiglet
import mac_change
import sys
sys.path.append("./")

banner = pyfiglet.figlet_format("zvadohacks console")
print(banner)

tools = ["change_mac", " net_spoof", "net_scan", "dns_spoof", "sniffer", "download_intercept"]

def user_input():
    command = input("->")
    if command == "exit":
        print("bye")
        sys.exit()
    if "run" in command:
        try:
            run_command = command.split()
            print(run_command)
            tool = run_command[1]
            options = run_command[2]
        except IndexError:
            print("[-] Please input command run command with options or check if the tool name is correct.")
            user_input()
        if tool not in tools:
            print("Pease insert correct tool name!")
        if tool in tools:
            if tool == "change_mac":
                print("whYYYYYYYYYYYYYYYYYYYYYYYY")
                interface = run_command[3]
                new_mac = run_command[5]
                print(interface)
                print(new_mac)
                mac_change.changeMac(interface, new_mac)
    if "help" in command:
        print("this is help")

while True:
    user_input()

