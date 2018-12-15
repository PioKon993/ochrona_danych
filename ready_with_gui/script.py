# -*- coding: utf-8 -*-
import sys
import os
import sys
import random
import math
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from tkinter.messagebox import showinfo
import tkinter as tk
from SzyfrujRSA import *
from WyborKluczy import *

root = tk.Tk()
root.title('Kodujemy!')
root.geometry('500x300')

informacja = "i"
publickeyfile = ""
privatekey_file = ""
    
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
    messagebox.showinfo("Sukces!", komunikat)

def code_file_popup():
    publickeyfile = filedialog.askopenfile(parent=root, mode='r',title='Choose a file with public key.')
    text_to_encode_file = filedialog.askopenfile(parent=root,mode='r',title='Choose a file with text.')
    text_to_encode = text_to_encode_file.read()
    messagebox.showinfo("Sukces!", "Tekst do zaszyfrowania: \n%s" % text_to_encode,)
    text_encoding(publickeyfile, text_to_encode)

def decode_file_popup():
    privatekey_file = filedialog.askopenfile(parent=root,mode='r',title='Choose a file with private key.')
    text_enc = filedialog.askopenfile(parent=root,mode='r',title='Choose a file with encoded text.')
    decoded_text = text_decoding(privatekey_file, text_enc)
    messagebox.showinfo("Sukces!","Odkodowany tekst: \n%s" % decoded_text)
    
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

    komunikat=("Stworzono klucze!\n"+"p = "+str(p) + "\nq = "+str(q)+"\ne = "+str(e)+"\nn = "+str(n)+"\nphi = "+str(phi))
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
