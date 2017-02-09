import socket
import textwrap
import struct

def main():
    check = dict()
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    while True:
        raw_data, addr = conn.recvfrom(443)
        dest_mac, source_mac, eth_proto, actual_data = ethernet_frame(raw_data)
        print("Enternet Frame: ")
        print("Destination: {}\nSource: {} \n protocol: {}".format(dest_mac, source_mac, eth_proto))
        text = open('Log',mode='a+')
        check[dest_mac] = 1
        print(len(check))
        text.write("Destination: {}\nSource: {} \n protocol: {}\n".format(dest_mac,source_mac,eth_proto))
#unpack the ethernet frame

def ethernet_frame(data):
    """Pass the captured frame"""
    # ! tells it is the network data
    # Starting 6 byte is the address of receiver
    # After it 6 byte is of sender
    # The 2 byte is used to tell the type of IP unsigned

    dest_mac, source_mac, proto = struct.unpack('! 6s 6s H', data[:14])
    return get_mac(dest_mac), get_mac(source_mac), socket.htons(proto), data[:14]

def get_mac(mac_raw):
    """Convert the mac in human readable format"""
    byte_str = map('{:02x}'.format, mac_raw)
    return ':'.join(byte_str).upper()

# get the detail of the IP Header
def ipv4_packet(data):
    version_header_length = data[0]
    version = version_header_length >> 4
    head_length = (version_header_length & 15)*4
    time_to_live, protocol, src, target = struct.unpack('! 8x B B 2x 4s 4s',data[:20])

main()
