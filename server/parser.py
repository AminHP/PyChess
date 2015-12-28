# python imports
from struct import pack, unpack

# project imports
from move import Move

class Parser:
    @staticmethod
    def decode(data):
        data = unpack('HBB', data)
        return data[0], Move((data[1] // 8, data[1] % 8), (data[2] // 8, data[2] % 8))

    @staticmethod
    def encode(turn, move):
        s = move.start[0] * 8 + move.start[1]
        e = move.end[0] * 8 + move.end[1]
        return pack('HBB', turn, s, e)
