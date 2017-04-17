import struct


class TCP:
    """This class is used to TCP header and data from the IPV4 data."""
    def __init__(self, data):
        self.src_port, self.dest_port, self.sequence, self.acknowledgement,\
            self.offest_reserved_flag = struct.unpack('! H H L L H', data[:14])
        self.offset = (self.offest_reserved_flag >> 12) * 4
        self.flag_urg = (self.offest_reserved_flag & 32) >> 5
        self.flag_ack = (self.offest_reserved_flag & 16) >> 4
        self.flag_psh = (self.offest_reserved_flag & 8) >> 3
        self.flag_rst = (self.offest_reserved_flag & 4) >> 2
        self.flag_syn = (self.offest_reserved_flag & 2) >> 1
        self.flag_fin = (self.offest_reserved_flag & 1)
        self.data = data[self.offset:]
