#!/usr/bin/python3
from scapy.all import *

# payload = "utyrioperituiosdfghjkidfghrytu4:wrtiorthyro9045678e345rfgtschji,UserId:123,PPPP:4324,abcdefghijklmnopqrs123457abhjr1:2ry78ui9orujh9045uijf567890erty,PPPP:4324,PPPP:333,ProductID:1234567890,"
# payload += "a"*500
payload="aaaaaaa:1111111,"
payload+="bbbbbbb:2222222,"
payload+="ccccccc:3333333,"
payload+="ddddddd:4444444,"
# payload = 'a'*798 + "she" + 'b'*1 + 'hi'
payload += 'c' * (1400 - len(payload))
pkt = Ether(src="3c:fd:fe:9e:7b:5c", dst="3c:fd:fe:9e:7b:85",type=0x0800)
pkt = pkt/IP(src="192.168.1.1", dst="192.168.1.2", id = 0xffff)
pkt = pkt/TCP(sport=5000, dport=56784, options=[('NOP',0),('NOP',0),('Timestamp', (1098453, 0))])
pkt = pkt/payload

wrpcap("pkt1.pcap",pkt)