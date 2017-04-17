import struct


class IPv4:

    def __init__(self, raw_data):
        version_header_length = raw_data[0]
        self.version = version_header_length >> 4
        self.head_length = (version_header_length & 15) * 4
        self.time_to_live, self.proto, src, target = struct.unpack\
            ('! 8x B B 2x 4s 4s', raw_data[:20])
        self.src = self.ipv4(src)
        self.target = self.ipv4(target)
        self.data = raw_data[self.head_length:]

    # Returns properly formatted IPv4 address
    def ipv4(self, addr):
        return '.'.join(map(str, addr))
