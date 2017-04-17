import socket
import struct
class Ethernet:
    """This class is used to extract the Ethernet frame from bit stream to
        human readable format.
    """
    def __init__(self, data):
        self.dest_mac, self.source_mac, self.proto \
            = struct.unpack('! 6s 6s H', data[:14]) # Unpacking the values
        self.proto = socket.htons(self.proto) # Convert the prototype to host to network
        self.dest_mac = self.get_mac(self.dest_mac)
        self.source_mac = self.get_mac(self.source_mac)
        self.data = data[14:]

    def get_mac(self, mac_raw):
        """Convert the mac in human readable format"""
        byte_str = map('{:02x}'.format, mac_raw)
        return ':'.join(byte_str).upper()



