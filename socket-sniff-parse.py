#Mack Howell
#Packet sniffer to GPIO
#For Linux - Sniffs all incoming and outgoing packets :)

import RPi.GPIO as GPIO
import time
import socket
import sys
from struct import *

# GPIO Setup Stuff
ignition = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ignition, GPIO.OUT)
current = GPIO.output(ignition, GPIO.LOW)
previous = current

def eth_addr(a):
    '''Convert a string of 6 characters of ethernet address into a dash separated hex string'''
    b = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(a[0]), ord(a[1]), ord(a[2]), ord(a[3]), ord(a[4]), ord(a[5]))
    return b

#create a AF_PACKET type raw socket (thats basically packet level)
#define ETH_P_ALL    0x0003          /* Every packet (be careful!!!) */
try:
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
except socket.error, msg:
    print 'Socket could not be created'
    sys.exit()

# receive a packet
while True:
    packet = s.recvfrom(1024)
    # event = packet.rstrip()
    # print event

    #packet string from tuple
    packet = packet[0]
    # while packet:
    #     print "GOT ONE"
    #     GPIO.output(7,GPIO.LOW)

    #parse ethernet header
    eth_length = 14
    eth_header = packet[:eth_length]
    eth = unpack('!6s6sH', eth_header)
    eth_protocol = socket.ntohs(eth[2])
    # print 'Destination MAC : ' + eth_addr(packet[0:6]) + ' Source MAC : ' + eth_addr(packet[6:12]) + ' Protocol : ' + str(eth_protocol)
    # print 'PROTOCOL: ' + str(eth_protocol)

    #Parse IP packets, IP Protocol number = 8
    if eth_protocol is 8:
        print "GOT ONE"
        GPIO.output(7,GPIO.HIGH)

        # #Parse IP header
        # #take first 20 characters for the ip header
        # ip_header = packet[eth_length:20+eth_length]
        # #now unpack them :)
        # iph = unpack('!BBHHHBBH4s4s', ip_header)
        # version_ihl = iph[0]
        # version = version_ihl >> 4
        # ihl = version_ihl & 0xF
        # iph_length = ihl * 4
        # ttl = iph[5]
        # protocol = iph[6]
    else:
        GPIO.output(7, GPIO.LOW)


        # pStream = str(protocol)
        # print 'PACKET: ' + str(protocol)

        # # My Counter
        # nlinePat = re.compile(r'\n')
        # bufferPos = 0
        # nlineCounter = 0
        # bl = nlinePat.split(str(protocol))
        # for line in bl:
        #     print(line.strip())
        #     nlineCounter += 1
        # print nlineCounter

# # GPIO Output Stuff
# while True:
#     current = GPIO.input(ignition)
#     if current != previous:
#         printState(current)
#     previous = current
#     time.sleep(0.1)
GPIO.cleanup()
