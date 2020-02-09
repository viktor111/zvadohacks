import pyfiglet
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
            tool = run_command[1]
            options = run_command[2]
        except IndexError:
            print("[-] Please input command with options")
            user_input()
        if tool not in tools:
            print("Pease insert correct tool name!")
        if tool in tools:
            if tool == "change_mac":
                from change_mac import mac_change
                def run():
                    mac_change
                run()

while True:
    user_input()

