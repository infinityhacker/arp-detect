#!/usr/bin/env python
#coding:utf-8
import logging
import sys
import subprocess
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy._all import *

if len(sys.argv[1:])!=1:
    print "Usage ./arp_detect.py [interface]"
    print "Example ./arp_dect.py eth0"
    print "Example will perform an ARP scan of the local submit to which eth0 is assigned"
    sys.exit()

interface=str(sys.argv[1])
ip=subprocess.check_output("ifconfig "+interface+" | grep 'netmask' | cut -d ' ' -f 10 | cut -d '.' -f 1-3",shell=True).strip()

prefix=ip.split('.')[0]+"."+ip.split('.')[1]+"."+ip.split('.')[2]+"."
 
for  addr in range(0,254):
    a=sr1(ARP(pdst=prefix+str(addr)),timeout=0.1,verbose=0)
    if a==None:
        pass
    else:
        print prefix+str(addr)
     
