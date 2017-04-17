import struct


class ICMP:

    '''This class is used to unpack the ICMP packet'''
    def __init__(self, data):
        self.type, self.code, self.checksum = struct.unpack('! B B H', data[:4])
        self.data = data[4:]
