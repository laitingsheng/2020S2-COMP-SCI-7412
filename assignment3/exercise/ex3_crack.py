#!/usr/bin/env python3

from itertools import product
from multiprocessing import Pool
from string import ascii_letters

from Crypto.PublicKey import RSA

with open("rsa_key.pub", "rb") as f:
    key = RSA.importKey(f.read(), 'PEM');

with open("ex3.enc", "rb") as f:
    encrypted = f.read()

def e(s):
    s = "".join(s)
    return s, key.encrypt(s.encode(), 0)[0]

def f(s):
    return encrypted == s[1]

if __name__ == "__main__":
    with Pool() as pool:
        ae = pool.map(e, product(ascii_letters, repeat=3))
    print([s[0] for s in filter(f, ae)])
