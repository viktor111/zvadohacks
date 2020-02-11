import netfilterqueue
import scapy.all as scapy

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        is_packet_request = scapy_packet[scapy.TCP].dport == 80
        is_packet_response = scapy_packet[scapy.TCP].sport ==80
        if is_packet_request:
        elif is_packet_response:
    packet.accept()
queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
