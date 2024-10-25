#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>
(if the format is not this one, the line must be skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C),
print these statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size>
(see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear or is not an integer, don’t
print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order

line list = [<IP Address>, -, [<date>], "GET /projects/260 HTTP/1.1",
<status code>, <file size>]
"""


import sys

# stores the count of all status codes in a dictionary
c = 0
tot_file_sz = 0
status_code_dict = {'200': 0,
                    '301': 0,
                    '400': 0,
                    '401': 0,
                    '403': 0,
                    '404': 0,
                    '405': 0,
                    '500': 0}

try:
    for line in sys.stdin:
        line_list = line.split(" ")
        if len(line_list) > 4:
            status_code = line_list[-2]
            file_sz = int(line_list[-1])
            # check if status code obtained is in dict and incr c by 1
            if status_code in status_code_dict.keys():
                status_code_dict[status_code] += 1
            # update tot_file_sz and count c
            tot_file_sz += file_sz
            c += 1
        if c == 10:
            c = 0  # reset count
            print("File size: {:d}".format(tot_file_sz), flush=True)
            for key, val in sorted(status_code_dict.items()):
                if val != 0:
                    print("{}: {}".format(key, val), flush=True)
except Exception as err:
    pass

finally:
    print(f"File size: {tot_file_sz}")
    for key, val in sorted(status_code_dict.items()):
        if val != 0:
            print("{}: {}".format(key, val), flush=True)
