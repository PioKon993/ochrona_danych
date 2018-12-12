# -*- coding: utf-8 -*-
import sys
import os
import sys
import random
import math
from tkinter import *
from tkinter import ttk
import tkinter as tk


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
    
def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("Sukces!")
    label = ttk.Label(popup, text=msg)
    label.pack(side="top", pady=10, padx=10)
    B1 = ttk.Button(popup, text="To świetnie!", command = popup.destroy)
    B1.pack()
    popup.mainloop()
    

if __name__ == '__main__':
    #p=generate_prime_number(2,1000000000)
    #q=generate_prime_number(2,1000000000)
    p=generate_prime_number(510,1000)
    q=generate_prime_number(510,1000)
    e=random.randint(1,100)
    n=p*q
    phi=(p-1)*(q-1)

    while NWD(e,phi)!=1:
        e=random.randint(1,100)

    komunikat=("Stworzono klucze!\n"+"p = "+str(p) + "q = "+str(q)+"\ne = "+str(e)+"n = "+str(n)+"phi = "+str(phi))
    d=extended_euklides(e,phi)
    publicKey=[e,n]
    privateKey=[d,n]
    generate_key('public', publicKey)
    generate_key('private', privateKey)

    popupmsg(komunikat)
    root.quit()
    
root = tk.Tk()
root.mainloop()
