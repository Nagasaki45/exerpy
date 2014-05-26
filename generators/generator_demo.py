'''
The goal is to read the log, filter only requests with status code
of 200, and sum the bytes of those requests.
'''

from time import time

FILENAME = 'access-log'

# the non generative way:
total = 0
with open(FILENAME) as f:
    for line in f:
        code, bytes = line.strip().split()[-2:]
        if code == '200' and bytes != '-':
            total += int(bytes)
print('Total bytes requested: {}'.format(total))

# using generators
with open(FILENAME) as f:
    rows = (line.strip() for line in f)
    only_200 = (r for r in rows if r.split()[-2] == '200')
    bytes_column = (r.split()[-1] for r in only_200)
    bytes = (int(b) for b in bytes_column if b != '-')
    print('Total bytes requested: {}'.format(sum(bytes)))
