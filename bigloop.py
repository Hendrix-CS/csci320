#!/usr/bin/python3

import sys

for arg in sys.argv:
    total = 0
    try:
        for i in range(int(arg)):
            total += i
        print(total)
    except:
        pass
