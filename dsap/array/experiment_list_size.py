"""Performs empirical testing of dynamic resizing of a Python list."""
import sys

try:
    n = int(sys.argv[1])
except:
    n = 100

import sys                                # provides getsizeof function
data = []
for k in range(n):                        # NOTE: must fix choice of n
    a = len(data)                         # number of elements
    b = sys.getsizeof(data)               # actual size in bytes
    print(f'Length: {a:3}; Size in bytes: {b:4}')
    data.append(None)                     # increase length by one
