#!/usr/bin/env python3

import sys

if len(sys.argv) < 3:
    print("none")
else:
    for X in reversed(sys.argv[1:]):
        print(X)
