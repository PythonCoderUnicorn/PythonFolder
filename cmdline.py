#!/bin/bash

import sys


cm ="""
 -----[ Command Line ]-----
"""
print(cm )

# target_url = str(input("Target URL: ")) 

try: 
    # python3 cmdline.py <url>
    target_url = sys.argv[1]

    print(f"target entered: {target_url} \n")

except:
    print("[!] Error --")
    print("[!] no argument: cmdline.py <arg> \n")





