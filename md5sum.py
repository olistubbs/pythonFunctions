#!/usr/bin/env python3.6

import hashlib

def md5sum(fileSrc):
    """md5sum function to provide the md5sum of fileSrc"""
    md5 = hashlib.md5()
    try:
        with open(fileSrc, "rb") as fd:
            while True:
                content = fd.read(2**20)
                if not content:
                    break
                md5.update(content)
    except IOError:
        print(fileSrc + " Not found")
        exit(1)
    return md5.hexdigest()
