import pyfiglet

banner = pyfiglet.figlet_format("zvadohacks console")
print(banner)

tools = ["change_mac", " net_spoof", "net_scan", "dns_spoof", "sniffer", "download_intercept"]

def read_command():
    command = input("->")

while True:
    read_command()
