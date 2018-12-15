# -*- coding: utf-8 -*-
from random import randrange
from tkinter import *
from tkinter import ttk
import tkinter as tk

root = tk.Tk()
root.title('Sprawdźmy liczbę!')
root.geometry('500x300')



rand_number = 0
rand_choice = ''

while(rand_choice != 't' and rand_choice != 'n'):
    rand_choice = input("Wylowować liczbę (T/N)?\n").lower()

    if(rand_choice == 't'):
        max_range = input('Podaj maksymalny zakres\n')
        rand_number = randrange(1, int(max_range), 2)
    elif(rand_choice == 'n'):
        rand_number = int(input('Podaj liczbę\n'))

tries = int(input('Podaj liczbę prób\n'))

print('Liczba: %d, prób: %d' % (rand_number, tries))

i = 0
is_prime = True

while(i < tries):
    a = randrange(2, rand_number)
    if(pow(a, rand_number - 1, rand_number) == 1):
        i+=1
    else:
        print('Liczba %d nie jest pierwsza' % (rand_number, ))
        is_prime = False
        break

if(is_prime):
    print('Liczba %d jest prawdopodobnie pierwsza' % (rand_number, ))


losujButton = ttk.Button(root, text ="Generuj klucz", command = actionGenerateKeys)
losujButton.place(x = 30, y = 30)

liczbaButton = ttk.Button(root, text ="Zakoduj plik", command = code_file_popup)
liczbaButton.place(x = 180, y = 30)

root.mainloop()
