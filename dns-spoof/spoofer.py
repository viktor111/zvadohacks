import netfilterqueue
import scapy.all as scapy
import subprocess
import optparse

def getArgs():
    parser = optparse.OptionParser()
    parser.add_option("-q", "--queue", dest="queueNum", help="Specify queue number.")
    (opt, arg) = parser.parse_args()
    if not opt.queueNum:
        parser.error("[-] Plase specify queue number. Use --help for more information.")

    return opt


def createQueue(queueNum):
    subprocess.call(["iptables", "-I", "FORWARD", "-j", "NFQUEUE", "--queue-num", queueNum])
    print("Queue created")


def processPacket(packet):
    scapyPacket = scapy.IP(packet.get_payload())
    print(scapyPacket.show())
    packet.accept()


opt = getArgs()
createQueue(opt.queueNum)
queue = netfilterqueue.NetfilterQueue()
queue.bind(int(opt.queueNum), processPacket)
queue.run()

