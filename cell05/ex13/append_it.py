#!/usr/bin/env python3

import sys

def main():
    if len(sys.argv) < 2:
        print("none")
        return

    for arg in sys.argv[1:]:
        if arg.endswith("ism"):
            continue
        print(arg + "ism")

main()
