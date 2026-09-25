#!/usr/bin/env python3

import sys

#---------------------------------------------------------------------
# Game Genie Code Decoder
# A git gist from https://gist.github.com/taotao54321/ce3f797bd7acc8f1eadb51eb0cce4313
# http://nesdev.com/nesgg.txt
#---------------------------------------------------------------------


GENIE_MAP_6 = (
    # addr
    None, 13, 14, 15,
      16, 21, 22, 23,
       4,  9, 10, 11,
      12, 17, 18, 19,
    # value
     0, 5, 6, 7,
    20, 1, 2, 3
)

GENIE_CHARS = "APZLGITYEOXUKSVN"

def to_bits(value, len_):
    assert len_ >= 1
    assert value < (1<<len_)
    return tuple(1 if (value&(1<<i)) else 0 for i in reversed(range(len_)))

def from_bits(bits):
    len_ = len(bits)
    value = 0
    for i, bit in enumerate(bits):
        value |= bit << (len_-1-i)
    return value

def seq_get(seq, i, default):
    if i is None: return default
    return seq[i]

# http://nesdev.com/nesgg.txt

def genie_ord(c):
    return GENIE_CHARS.index(c)

def genie_shuffle(bits, map_):
    return tuple(seq_get(bits, map_.get(i), 0) for i in range(len(bits)))

def decode_game_genie_code(code):
    map_ = dict((k,v) for k,v in enumerate(GENIE_MAP_6))

    cipher = sum((to_bits(genie_ord(c),4) for c in code), ())
    plain  = genie_shuffle(cipher, map_)

    addr  = 0x8000 | from_bits(plain[0:16])
    value = from_bits(plain[16:24])
    print("0x{:04X}\t0x{:02X}".format(addr, value))
    return (addr,value)

# PUT YOUR CODE DOWN HERE IN THE MAIN FUNCTION !!!!!!

def main(args):
    print("This program only parses 6 character game genie codes")

    args.pop(0)

    for arg in args:
        print(arg)

        (addr, value) = decode_game_genie_code(arg.upper())
        print(f"Address = {hex(addr)}")
        print(f"Value   = {hex(value)}")


if __name__ == "__main__":
    main(sys.argv)
