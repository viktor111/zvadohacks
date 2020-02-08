import subprocess
import scapy
import optparse
import netfilterqueue


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
    print(packet)
    packet.drop()


opt = getArgs()
createQueue(opt.queueNum)
queue = netfilterqueue.NetfilterQueue()
queue.bind(int(opt.queueNum), processPacket)
queue.run()

