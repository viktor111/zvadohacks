import netfilterqueue


def processPacket():
    scapyPacket = scapy.IP(packet.get_payload())
    packet.accept()


