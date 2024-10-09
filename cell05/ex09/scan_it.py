#!/usr/bin/env python3

import sys

def main():
    if len(sys.argv) != 3:
        print("none")
        return

    keyword, search_string = sys.argv[1], sys.argv[2]
    
    count = search_string.split().count(keyword)

    print(count if count > 0 else "none")

main()
