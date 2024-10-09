#!/usr/bin/env python3

import sys

def main():
    if len(sys.argv) < 2:
        print("none")
        return

    parameters = sys.argv[1:]

    print(f"parameters: {len(parameters)}")

    for parameter in parameters:
        print(f"{parameter}: {len(parameter)}")

main()
