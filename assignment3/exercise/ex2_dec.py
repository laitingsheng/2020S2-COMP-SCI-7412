#!/usr/bin/env python3

from itertools import cycle

enc = "evfsgm aj vgfjicf oekf mrvud qqzvea"
key = cycle(map(ord, "ecms"))

print(
    " ".join(
        "".join(
            chr((ord(v) - k) % 26 + ord('a'))
            for v, k in zip(word, key)
        )
        for word in enc.split()
    )
)
