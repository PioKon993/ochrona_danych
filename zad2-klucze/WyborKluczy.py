# -*- coding: utf-8 -*-
import sys
import os
import sys
import random

def extended_euklides(a, n):

    p0, p1, a0, n0 = 0, 1, a, n
    q, r = n0 // a0, n0 % a0
    while r:
        t = p0 - (q * p1)

        if t >= 0:
            t = t % n
        else:
            t = n - ((-t) % n)
        p0, p1, n0, a0 = p1, t, a0, r
        q, r  = n0 // a0, n0 % a0
    return p1

def NWD(a,b):
    while True:
        r = a % b
        if not r:
            return b
        a, b = b, r

def generate_key(kind_of_key,values):
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

    #p=random.randint(1,1000000000)
    #q=random.randint(1,1000000000)
    p=random.randint(1,20)
    q=random.randint(1,40)
    e=random.randint(1,100)
    n=p*q
    phi=(p-1)*(q-1)

    while NWD(e,phi)!=1:
        e=random.randint(1,100)

    d=extended_euklides(e,phi)
    publicKey=[e,n]
    privateKey=[d,n]
    generate_key('public', publicKey)
    generate_key('private', privateKey)
