import dpkt, pcap

pc = pcap.pcap()
pc.setfilter('icmp')
for timestamp, packet in pc:
    print dpkt.ethernet.Ethernet(pkt)
