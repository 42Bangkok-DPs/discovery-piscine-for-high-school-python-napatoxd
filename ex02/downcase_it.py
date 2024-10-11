#!/usr/bin/env python3
import sys

def downcase_it(string):
    return string.lower()

def main():
    parameters = sys.argv[1:]

    if not parameters:
        print("none")
    else:
        for param in parameters:
            print(downcase_it(param))

main()
