#!/usr/bin/env python3

from itertools import product

def diff(cs):
    return (ord(cs[0]) - ord(cs[1])) % 26

def run(s1, s2):
    re = list(map(diff, zip(s1, s2)))
    conv = "".join(chr(ord("a") + d) for d in re)
    print(f"{s1}:{s2} {re} {conv}")

lists = [("vgfjicf", "tuesday")] + list(
    product(["evfsgm", "qqzvea"], ["monday", "friday", "sunday"])
)
for s1, s2 in lists:
    run(s1, s2)
