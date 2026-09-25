#!/usr/bin/env python3
from itertools import product

def main():
    checked=0
    for auth,tenant,idempotency,version_ok,write in product((False,True), repeat=5):
        admitted = (not write) or (auth and tenant and idempotency and version_ok)
        if write and admitted:
            assert auth and tenant and idempotency and version_ok, 'write admitted without full preconditions'
        checked+=1
    print(f'write admission model: {checked} states')
if __name__=='__main__': main()
