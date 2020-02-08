import pyfiglet
import sys
sys.path.append("./")
import change_mac


banner = pyfiglet.figlet_format("Hello HACKERS!")
print(banner)

tools = ["change_mac", " net_spoof", "net_scan", "dns_spoof", "sniffer", "download_intercept"]

def user_input():
    command = input("->")
    if command == "exit":
        print("bye")
        sys.exit()
    if "run" in command:
        run_command = command.split()
        tool = run_command[1]

while True:
    user_input()

