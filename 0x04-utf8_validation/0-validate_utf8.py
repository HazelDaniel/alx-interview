#!/usr/bin/python3
"""this module attempts a UTF-8 Validation"""


def get_leading_set_bits(num):
    """returns the number of leading set bits (1)"""
    set_bits = 0
    helper = 1 << 7
    while helper & num:
        set_bits += 1
        helper = helper >> 1
    return set_bits


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""
    bit_count = 0
    for i in range(len(data)):
        if bit_count == 0:
            bit_count = get_leading_set_bits(data[i])

            if bit_count == 0:
                continue
            if bit_count == 1 or bit_count > 6:
                return False
        else:
            """one last check: if the current byte has format 10xxxxxx"""
            if not (data[i] & (1 << 7) and not (data[i] & (1 << 6))):
                return False
        bit_count -= 1
    return bit_count == 0
