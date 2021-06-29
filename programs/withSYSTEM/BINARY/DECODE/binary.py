#!/usr/bin/env python3

import sys


if __name__ == "__main__":
    if len(sys.argv) != 1 and len(sys.argv) <= 3:
        if sys.argv[1] in ('-b', '--binary'):
            n = int(sys.argv[2].replace(' ', ''), 2)
            print(n.to_bytes((n.bit_length() + 7) // 8, 'big').decode())
    else:
        print("Example: decode -b '10000001'")