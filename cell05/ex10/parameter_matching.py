#!/usr/bin/env python3

import sys

def main():
    if len(sys.argv) != 2:
        print("none")
        return

    parameter = sys.argv[1]

    input1 = input("What was the parameter? ")

    if input1 == parameter:
        print("Good job!")
    else:
        print("Nope, sorry...")

main()
