#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) != 3:
        print('none')
        return
    
    start = int(sys.argv[1])
    end = int(sys.argv[2])
        
    result = list(range(start, end + 1))
        
    print(result)

main()
