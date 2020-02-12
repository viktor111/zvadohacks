# zvadohacks

zvadohacks are tools build with python for web scouting sniffing and pen testin

## console
 The console is work in process console which will allow the user to run the tools without having to be in the directory of the tool. It is currently in experimental stage so you should run the tool from the directory.

## Tools
 
```
mac-change
```
Change your mac address just with a simple command whenever you want.
```
net-scan
```
Scan all the devices on your wifi and diplay infromataion such as ip address mac address and manufacturer (make sure to include /24 at the end of the ip or you will not see all devices.)
```
net-spoof
```
Trick the router and the victim by sending ARP packet to both with the MAC address of each other and become man in the middle. (you must enable forwarding and if using wifi must have wifi chpset wich can be in monitor mode)
```
sniffer
```
Once you used net spoof to become man in the middle you can use sniffer tool to watch for incoming http requests (GET, POST, etc) and extract data like url username and password.
```
net-stop
```
net-stop creates a queue in wich incoming packets to the traget with the spoofer are held and dropped so the target never gets a response.

```
dns-spoof
```
Captures and modifes DNS response so you can redirect the target IP to a new host

### Usage
mac-change
```
cd ../change-mac
sudo python3 mac_change.py -i [intefrace goes here] -m [new mac goes here]
```
net-scan
```
cd ../net-scan
sudo python3 netscan.py -i [IP address goes here]
```
net-spoof
```
cd ../net-spoof
sudo python3 netspoof.py -i [-target IP goes here] -r [router IP goes here]
```
sniffer
```
cd ../sniffer
sudo python3 sniffer.py -i [your interface goes here]
```
net-stop
```
cd ../net-stop
sudo python3 stopper.py -q [number of queue goes here]
```
dns-spoofer
```
cd ../dns-spoof
sudo python spoofer.py -q [number of queue goes her] -t [0 for no 1 yes] --oh [host to be spoofed goes here] -rh [redirect host goes here]
after you exit run  iptables --flush to disband all the queues
```
download-intercept
```
Still being worked on will update once done.
```

## Prerequisites

```
- python 2.7
- python 3.0
- git
- pip
- pip3 install mac-vendor-lookup
- pip install --pre scapy[complete]
- pip install NetfilterQueue (if you get error try running this first - sudo apt-get install libnetfilter-queue-dev libnetfilter-queue1)
```

### Installing


```
clone repo
```
```
cd into cloned repo
```
```
to run a tool use python3 [name of tool] [options]
```

## Built With

* [Python 2.7/3](https://www.python.org/) - Language used to write the tools

* [Ubuntu Linux](https://ubuntu.com/) - OS used

## Authors

* **Viktor Draganov** - *Initial work* - [viktor111](https://github.com/viktor111)

