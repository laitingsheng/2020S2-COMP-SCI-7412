#!/usr/bin/env python3

mapping = {
    e: d
    for enc, dec in (
        ("fc", "hi"),
        ("kfggxt", "cheers"),
        ("fow", "how"),
        ("nxg", "are"),
        ("qoa", "you"),
        ("ixgg", "free"),
        ("dfct", "this"),
        ("ixcjnq", "friday"),
        ("sczfd", "night"),
        ("hoh", "bob"),
        ("grgxqdfcsz", "everything"),
        ("pbnsscsz", "planning"),
        ("loxg", "more")
    )
    for e, d in zip(enc, dec)
}

with open("ex1.enc", "r") as rf:
    with open("ex1.dec", "w") as wf:
        wf.write("".join(mapping.get(e, e) for e in rf.read()))
