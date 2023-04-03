import subprocess
import socket

def discover_device_ip(mac_address):
    # Send an ARP request to the local network to find the device
    arp_result = subprocess.check_output(['arp', '-a'])
    arp_lines = arp_result.decode().splitlines()
    
    # Iterate over the ARP table to find the device's IP address
    for line in arp_lines:
        if mac_address in line:
            ip_address = line.split()[1].strip('()')
            
            # Verify that the IP address is valid by trying to resolve the hostname
            try:
                socket.gethostbyaddr(ip_address)
                return ip_address
            except socket.herror:
                pass
    
    # If the device is not found, return None
    return None
finding_device = discover_device_ip("78:45:58:77:3c:92")
if finding_device:
    print(f"found ip for mac {finding_device}")
else:
    print(f"not found ip for mac {finding_device}")
