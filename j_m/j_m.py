#!/usr/bin/env python3

import sys
import pathlib
import os

DELIM = ","


def process_file(fname):
    npath = fname.with_suffix(fname.suffix + ".csv")
    data = ""

    with open(fname, "r") as file:
        for line in file.readlines():
            spl = line.split(" ")
            spl = filter(lambda v: v != "", spl)
            data += DELIM.join(spl)

    with open(npath, "w") as file:
        file.write(data)


def process_folder(fname):
    for file in os.listdir(fname):
        fpath = pathlib.Path(fname) / file
        if fpath.suffix == ".j_m":
            process_file(fpath)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("usage: python j_m.py <FILE>")

    inpath = pathlib.Path(sys.argv[1])

    if inpath.is_file():
        process_file(inpath)

    elif inpath.is_dir():
        process_folder(inpath)
