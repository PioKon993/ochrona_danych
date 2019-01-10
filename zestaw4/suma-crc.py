from tkinter import *
from tkinter import messagebox


def suma_crc(data, input_divider):
    binaries = get_binaries_from_str(data)
    divider = get_divider_from_input(input_divider)

    # binaries = "11010011101110"
    # divider = "1011"

    divider_length = len(divider)
    n = divider_length - 1
    binaries += "0" * n
    binaries_result = list(binaries)

    i = 0
    while i < (len(binaries) - divider_length):
        if binaries_result[i] == "1":
            for x in range(divider_length):
                bit = logical_xor(binaries_result[i + x], divider[x])
                binaries_result[i + x] = bit
            # print(''.join(binaries_result))
        i += 1

    str_binaries_result = ''.join(binaries_result)
    crc_sum = str_binaries_result[-n:]
    return crc_sum


def get_divider_from_input(input_divider):
    full_divider = get_binaries_from_str(input_divider)
    max_divder_length = 8
    if len(full_divider) > 8:
        divider = full_divider[-max_divder_length:]
    else:
        divider = ("0" * (max_divder_length - len(full_divider)) + full_divider)
    return divider


def get_binaries_from_str(data):
    return ' '.join(format(ord(x), 'b') for x in data)


def logical_xor(a, b):
    if a == b:
        return "0"
    else:
        return "1"


def handle_sum_crc():
    sum = suma_crc(e1.get(), e2.get())
    messagebox.showinfo("Suma CRC", "Obliczona suma CRC to:\n" + sum)


if __name__ == '__main__':
    # print(suma_crc("siema", "5"))

    master = Tk()
    master.title("Suma CRC")
    master.geometry("500x120")
    Label(master, text="Podaj ciąg znaków").grid(row=0)
    Label(master, text="Podaj dzielnik do obliczenia sumy CRC (max 8 bitów)").grid(row=1)

    e1 = Entry(master)
    e2 = Entry(master)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    Button(master, text='oblicz sume CRC', command=handle_sum_crc).grid(row=3, column=1, sticky=W, pady=4)

    mainloop()
