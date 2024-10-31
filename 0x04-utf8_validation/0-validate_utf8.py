#!/usr/bin/python3
"""
A method that determines if a given data
set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """Return true for a valid UTF-8 code"""
    nbytes = 0

    b1 = 1 << 7
    b2 = 1 << 6

    for byte in data:
        b = 1 << 7
        if nbytes == 0:
            while b & byte:
                nbytes += 1
                b = b >> 1
            if nbytes == 0:
                continue
            if nbytes == 1 or nbytes > 4:
                return False
        else:
            if not (byte & b1 and not (byte & b2)):
                return False
        nbytes -= 1
    if nbytes == 0:
        return True
    else:
        return False
