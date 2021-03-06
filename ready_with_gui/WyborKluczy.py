# -*- coding: utf-8 -*-
import sys
import os
import sys
import random
import math

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

def generate_prime_number(range_min, range_max):

    if range_min<2:
        print('Range min must be greater or equal than 2')
        sys.exit(1)

    prime_number=0
    prime_number_candidate=0
    isPrime=False

    while isPrime==False:
        prime_number_candidate=random.randint(range_min, range_max)
        if check_is_prime(prime_number_candidate)!=False:
            isPrime=True
            prime_number=prime_number_candidate
    return prime_number

def check_is_prime(number):

    for i in range(2,int(math.sqrt(number)+1)):
        if number % i == 0:
            return False
    else:
        return True


    

