# -*- coding: utf-8 -*-
from random import randrange
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo
from tkinter import simpledialog
from tkinter.simpledialog import askinteger
import tkinter as tk
import sys

root = tk.Tk()
root.withdraw()
root.title('Sprawdźmy liczbę!')
root.geometry('500x300')

result = 'yes'

while result:
    
    rand_number = 0
    rand_choice = messagebox.askyesno("Losujemy?", "Wylosować liczbę?", parent=root)

    if rand_choice:
        max_range = simpledialog.askinteger("Zasięg","Podaj maksymalny zakres",parent=root,minvalue=0)
        rand_number = randrange(1, int(max_range), 2)
    else:
        rand_number = simpledialog.askinteger("ZLiczba","Podaj liczbę",parent=root,minvalue=1)

    tries = simpledialog.askinteger("Próby","Podaj ilość prób",parent=root,minvalue=1)

    messagebox.showinfo("Działajmy!", 'Liczba: %d, prób: %d' % (rand_number, tries))

    i = 0
    is_prime = True

    while(i < tries):
        a = randrange(2, rand_number)
        if(pow(a, rand_number - 1, rand_number) == 1):
            i+=1
        else:
            messagebox.showinfo("Wynik", 'Liczba %d nie jest pierwsza' % (rand_number, ))
            is_prime = False
            break  

    if(is_prime):
        messagebox.showinfo("Brawo!", "Liczba %d jest prawdopodobnie pierwsza'" % (rand_number, ))
    result = messagebox.askyesno("Jeszcze?", "Czy chcesz spróbować jeszcze raz?", parent=root)
    if result == 'no':
        root.destroy()
        exit()
        
        
root.mainloop()
