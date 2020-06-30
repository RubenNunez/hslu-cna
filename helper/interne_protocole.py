import struct
import sys

from netaddr import IPAddress

def ip2bin(ip):
    print('.'.join([bin(int(x)+256)[3:] for x in ip.split('.')]))


def bin2ip(ip):
    print('.'.join(str(int(ip.replace('.','')[i:i+8], 2)) for i in range(0, 32, 8)))


def netmask2cidr(mask):
    print(IPAddress(mask).netmask_bits())


def cidr2netmask(prefix):
    print('.'.join([str((0xffffffff << (32 - int(prefix)) >> i) & 0xff)
                    for i in [24, 16, 8, 0]]))


def cidr2hosts(prefix):
    print('Total Hosts in Subnet: ' + str((2**(32- prefix)) - 2))