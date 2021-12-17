import aocd
from session.session import get_session  # returns personal session
import heapq
from math import inf
import numpy as np

#alright, first off, this problem sounds AWFUL
my_session = get_session()
day = 16
example = False

if example:
    dta = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""
else:
    dta = aocd.get_data(session=my_session, day=day, year=2021)


class packetDecoder():
    def __init__(self, input_string):
        self.input_string = input_string
        self.bin_str = None
        self.version = None
        self.type = None  # I know, but whatever'
        self.length_type = None
        self.subpacket_len = None
        self.sub_packet_count = None
        self.literal_int = None
        self.sub_packet_start_index = None

    @staticmethod
    def hex_to_bin(h):
        return bin(int(h, 16))[2:].zfill(4)

    def hex_str_to_bin(self):
        out = ''
        for c in [char for char in self.input_string]:
            out += self.hex_to_bin(h=c)
        self.bin_str = out


    def get_version(self):
        """First three characters are version, leading with most significant digit"""
        self.version = int(self.bin_str[0:3],2)

    def get_type(self):
        """First three characters are version, leading with most significant digit"""
        self.type = int(self.bin_str[3:6],2)

    def get_length_type(self):
        self.length_type = self.bin_str[7]

    def evaluate_literal(self):
        literal = self.bin_str[6:]
        chunk_len = 5
        unchunked = ''
        for i in range(0, len(literal), chunk_len):
            chunk = literal[i:i + chunk_len]
            if chunk[0] == '1':
                unchunked += chunk[1:]
            else:
                chunk = literal[i:]
                chunk = chunk.rstrip('0')
                unchunked += chunk[1:]
                break
        return unchunked

    def evaluate_type(self):
        if self.type == 4:
            literal_str = self.evaluate_literal()
            self.literal_int =  int(literal_str,2)
        if self.type ==6:
            print('operator')

    def evaluate_length_type(self):
        if self.length_type=='0':
            self.subpacket_len = int(self.bin_str[7:7 + 15],2)
            self.sub_packet_start_index = 7 + 15
        else:
            self.sub_packet_count = int(self.bin_str[7:7+11],2)
            self.sub_packet_start_index = 7+11

    def get_sub_packet(self):
        #THIS PART IS WRONG
        first_packet = self.bin_str[self.sub_packet_start_index - 7:self.sub_packet_start_index]
        second_packet = self.bin_str[self.sub_packet_start_index:(self.subpacket_len-self.sub_packet_start_index)]
        return first_packet, second_packet

    def decode(self):
        self.hex_str_to_bin()
        self.get_version()
        self.get_type()
        self.get_length_type()
        self.evaluate_type()
        self.evaluate_length_type()


decoder = packetDecoder(input_string='D2FE28')
decoder.hex_str_to_bin()

#tests
assert decoder.bin_str=='110100101111111000101000', 'whoopsy poopsy'
decoder.get_version()
assert decoder.version==6, 'wrong version baby'
decoder.get_type()
assert decoder.type==4, 'wrong type baby'
assert decoder.evaluate_literal()=='011111100101', 'wrong literal'
decoder.decode()
assert decoder.literal_int == 2021

decoder = packetDecoder(input_string='38006F45291200')
decoder.decode()
assert decoder.type==6, 'wrong type'
assert decoder.length_type == '0','wrong length type'
assert decoder.subpacket_len == 27, 'wrong subpacket length'
decoder.get_sub_packet()
