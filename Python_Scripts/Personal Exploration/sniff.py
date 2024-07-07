# Wildly unfinished script to create a socket to sniff traffic on a local machine
# I'm in the process of making a simple little daemon to watch for TCP handshakes and send a toast notification. 
# Ideally, the toast notification would be color coded to indicate if the handshake completed when initiated from a remote host instead of the client
# This is mostly for me to just test and explore what I can accomplish within Python.


import socket
import struct
import textwrap



def main():
    connection = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

    while True:
        raw_data, addr = connection.recvfrom(65536)
        dest_MAC, src_MAC, eth_protocol, data = ethernetFrame(raw_data)
        print('\nEthernet Frame: ')
        print('Destination :{}, Source{}, Protocol: {}'.format(dest_MAC, src_MAC, eth_protocol))

#Unpack Eth frame. Type is 0x0800 for IPv4 frames. Focused most on IPv4

def ethernetFrame (data):
    dest_MAC, src_MAC, protocol = struct.unpack('! 6s 6s H', data[:14])
    return getMACAddr(dest_MAC), getMACAddr(src_MAC), socket.htons(protocol), data[14:]
 #Call function to format MAC from bytes to human readable
 #First 14 bytes is the header information, remainder 14 is the payload. Ignoring CRC for now

def getMACAddr(bytes_addr):
    bytes_str = map('{:02x}'.format, bytes_addr) #i.e. aa:bb:11
    mac_Addr = ':'.join(bytes_str).upper() #i.e AA:BB:11
    return mac_Addr

main()


