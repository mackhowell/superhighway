from scapy.all import *

m_iface = "eth0"
m_dst = "192.168.0.1"

def print_summary(pkt):
  print pkt.summary()

def plain_sniff():
  sniff(iface = m_iface, count = 10, filter = "icmp and src {0}".format(m_dst), prn = print_summary)
