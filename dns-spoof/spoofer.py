import netfilterqueue
import scapy.all as scapy
import subprocess
import optparse

def getArgs():
    parser = optparse.OptionParser()
    parser.add_option("-q", "--queue", dest="queueNum", help="Specify queue number.")
    parser.add_option("-t", "--test", dest="test", help="Test only on your machine 0 for no 1 for yes.")
    (opt, arg) = parser.parse_args()
    if not opt.queueNum:
        parser.error("[-] Plase specify queue number. Use --help for more information.")
    if not opt.test:
        parser.error("[-] Plase specify test option. Use --help for more information.")
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
    scapyPacket = scapy.IP(packet.get_payload())
    if scapyPacket.haslayer(scapy.DNSRR):
        print(scapyPacket.show())
    packet.accept()


opt = getArgs()
createQueue(opt.queueNum, int(opt.test))
queue = netfilterqueue.NetfilterQueue()
queue.bind(int(opt.queueNum), processPacket)
queue.run()

