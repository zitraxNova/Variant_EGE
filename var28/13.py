from ipaddress import *

net = ip_network('17.223.13.15/255.255.255.240', 0)
for ip in net:
    ip2 = bin(int(ip))[2:].zfill(32)
    if ip2.count('1') <= 13:
        print(ip)

# 17.223.13.8
#17223138