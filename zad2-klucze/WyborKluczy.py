# -*- coding: utf-8 -*-
import sys
import os
import sys
import random

def NWD(a,b):
    while True:
        r = a % b
        if not r:
            return b
        a, b = b, r

def write_to_file(kind_of_key,values):
    if (kind_of_key == 'public'):
        f = open('public.key', 'w')
        for x in range(0,len(values)):
            f.write(str(values[x])+'\n')
        f.close()
    else:
        f = open('private.key', 'w')
        for x in range(0,len(values)):
            f.write(str(values[x])+'\n')
        f.close()

if __name__ == '__main__':
    p=random.randint(1,1000000000)
    q=random.randint(1,1000000000)
    e=random.randint(1,100)
    n=p*q
    phi=(p-1)*(q-1)
    print(p,q,e,n,phi)
    while NWD(e,phi)!=1:
        e=random.randint(1,100)
    print(e,phi)
    d=e*(phi-1)%phi
    publicKey=[e,n]
    privateKey=[d,n]
    write_to_file('public',publicKey)
    write_to_file('private',privateKey)
