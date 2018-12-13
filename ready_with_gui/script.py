# -*- coding: utf-8 -*-
import sys
import os
import sys
import random
import math
from tkinter import *
from tkinter import ttk
import tkinter as tk
from SzyfrujRSA import *
from WyborKluczy import *

root = tk.Tk()
    
def popupmsg(msg, title, buttonText):
    popup = tk.Tk()
    popup.wm_title(title)
    label = ttk.Label(popup, text=msg)
    label.pack(pady=10, padx=10)
    B1 = ttk.Button(popup, text= buttonText, command = popup.destroy)
    B1.pack()
    popup.mainloop()
    
def actionGenerateKeys():
    actionButton.config(state="disabled")
    popupmsg(komunikat, "Sukces!", "Dziękuję Panie Programie")

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

    komunikat=("Stworzono klucze!\n"+"p = "+str(p) + "q = "+str(q)+"\ne = "+str(e)+"n = "+str(n)+"\nphi = "+str(phi))
    d=extended_euklides(e,phi)
    publicKey=[e,n]
    privateKey=[d,n]
    generate_key('public', publicKey)
    generate_key('private', privateKey)


actionButton = ttk.Button(root, text ="Generuj klucz", command = actionGenerateKeys)
actionButton.pack()

codeButton = ttk.Button(root, text ="Generuj klucz", command = actionGenerateKeys)
codeButton.pack()
root.quit()
    
root.mainloop()
