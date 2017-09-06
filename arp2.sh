#！/bin/bash
if ["$#" -ne 1]:then
  echo "Usage ./arping.sh [file]"
  echo "Example ./arping .sh file1"
  echo "Example will perform an ARP scan of the local subnet to which etho0 is assigned"
  exit
fi
file=$1
for addr in $(cat $file);do
 arping -c 1 $addr | grep "bytes from " | cut -d "" -f 5| cut -d "(" -f 2| cut -d ")" -f 1
done
