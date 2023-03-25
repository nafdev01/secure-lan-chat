import ipaddress

ip_interface = ipaddress.IPv4Interface('192.168.0.1/255.255.255.0')
cidr_notation = ip_interface.network.prefixlen

print(cidr_notation)
