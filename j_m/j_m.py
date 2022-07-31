#!/usr/bin/env python3

import sys

fname = sys.argv[1]

output = ""

with open(fname, "r") as file:
    for line in file.readlines():
        spl = line.split(" ")
        spl = filter(lambda v: v != "", spl)
        output += ";".join(spl)

print(output)
