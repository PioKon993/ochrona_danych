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
root.title('Kudujemy!')
root.geometry('500x300')

informacja = "i"
    
def popupmsg(msg, title, buttonText):
    popup = tk.Tk()
    popup.wm_title(title)
    label = ttk.Label(popup, text=msg)
    label.pack(pady=10, padx=10)
    B1 = ttk.Button(popup, text= buttonText, command = popup.destroy)
    B1.pack()
    popup.mainloop()

def codingAction():
    code_file()
    text_encoding(text_to_encode)
    
def actionGenerateKeys():
    actionButton.config(state="disabled")
    popupmsg(komunikat, "Sukces!", "Dziękuję Panie Programie")

def code_file_popup():
    encode_file()
    codeButton.config(state="disabled")
    popupmsg(informacja, "Sukces!", "Dziękuję Panie Programie")

def decode_file_popup():
    decodeButton.config(state="disabled")
    decode_file()
    popupmsg(informacja, "Sukces!", "Dziękuję Panie Programie")
    
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
    actionButton.place(x = 30, y = 30)

    codeButton = ttk.Button(root, text ="Zakoduj plik", command = code_file_popup)
    codeButton.place(x = 180, y = 30)

    decodeButton = ttk.Button(root, text ="Dekoduj plik", command = decode_file_popup)
    decodeButton.place(x = 320, y = 30)
    root.quit()
        
    root.mainloop()
