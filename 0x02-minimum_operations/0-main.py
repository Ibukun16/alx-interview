#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 16
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 18
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 20
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 19
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 2147483640
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))