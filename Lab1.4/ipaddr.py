from ipaddress import IPv4Network
from random import randint

class IPv4RandomNetwork(IPv4Network):
    def __init__(self):
        ipaddr = randint(0x0B000000, 0xDF000000)
        netmask = randint(0, 24)
        IPv4Network.__init__(self, (ipaddr, netmask), strict=False)

    def regular(self):
        # return self.is_global
        return not (self.is_reserved or self.is_private or self.is_loopback or self.is_link_local)

    def key_value(self):
        return int(self.hostmask)*2**32 + int(self.network_address)

    def get_subnet(self):
        return self


ipList = []
while len(ipList) < 50:
    subnet = IPv4RandomNetwork()
    if subnet.regular() and subnet not in ipList:
        ipList.append(subnet.get_subnet())


sorted_ipList = sorted(ipList, key=lambda x: x.key_value())

print(ipList)
print(sorted_ipList)
print(len(ipList))
