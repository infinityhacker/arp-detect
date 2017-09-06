#!/usr/bin/env python
coding:utf-8
import logging
import sys
import subprocess
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

if len(sys.argv[1:])!=2:
  print "Usage ./arp_detect.py [interface]"
  print "Example ./arp_dect.py eth0"
  print "Example will perform an ARP scan of the local submit to which eth0 is assigned"
  sys.exit()
  
filename=sys.argv[1]
file=open(filename,'r')
 for  addr in file:
  a=sr1(ARP(pdst=addr.strip()),timeout=0.1,verbose=0)
  if answer==None:
    pass
   else:
    print addr.strip()
