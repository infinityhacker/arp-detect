！/bin/bash
if [ "$#" -ne 1 ];then
  echo "Usage ./arping.sh [interface]"
  echo "Example ./arping .sh eth0"
  echo "Example will perform an ARP scan of the local subnet to which etho0 is assigned"
  exit
fi
interface=$1
prefix=$(ifconfig  $interface | grep "netmask" | cut -d ' ' -f 10 | cut -d '.' -f 1-3)
for addr in $(seq 1 254);do
 arping -c 1 $prefix.$addr  | grep "Unicast" | cut -d ' ' -f 4
done
