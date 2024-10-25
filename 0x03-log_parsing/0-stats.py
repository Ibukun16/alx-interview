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


# create a dictionary of all status codes
status_code_dict = {'200': 0,
                    '301': 0,
                    '400': 0,
                    '401': 0,
                    '403': 0,
                    '404': 0,
                    '405': 0,
                    '500': 0}

tot_size = 0
c = 0  # keep count of the number lines counted

try:
    for line in sys.stdin:
        arg = line.split(" ")
        if len(arg) > 4:
            status_code = arg[-2]
            file_size = int(arg[-1])

            # if status code is in the dictionary, incr c by 1
            if status_code in status_code_dict.keys():
                status_code_dict[status_code] += 1

            # update total size
            tot_size += file_size

            # Update the count of lines
            c += 1

        if c % 10 == 0:
            c = 0  # reset count
            print(f"File size: {tot_size}")
            for key, val in sorted(status_code_dict.items()):
                if val != 0:
                    print(f"{key}: {val}")

except Exception as err:
    pass
finally:
    print("File size: {tot_size}")
    for key, val in sorted(status_code_dict.items()):
        if val != 0:
            print(f"{key}: {val}")
