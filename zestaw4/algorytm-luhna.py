from tkinter import *
from tkinter import messagebox


def create_control_num(number):
    if not number.isdigit():
        raise ValueError("Podany ciąg znaków posiada nieodpowiednie znaki")
    number = str(number)
    sum = 0
    i = 0
    while i < len(number):
        add_to_sum = int(number[i]) * get_weight(i)
        if add_to_sum > 9:
            add_to_sum = int(str(add_to_sum)[0]) + int(str(add_to_sum)[1])

        sum += add_to_sum
        i += 1

    control_num = sum % 10
    if control_num != 0:
        control_num = 10 - control_num

    return control_num


def get_weight(index):
    weight = 1
    if index % 2 == 0:
        weight = 2
    return weight


def create_luhn_number(number):
    control_num = create_control_num(number)
    return str(number) + "-" + str(control_num)


def validate_control_number(number):
    number = str(number)
    if "-" not in number:
        raise ValueError(
            "Niepoprawny format - ciąg cyfr oraz cyfra kontrolna powinny być oddzielone myślnikiem np. 123-4")

    numbers = number.split("-")[0]
    control_num = number.split("-")[1]

    validation_control_num = create_control_num(numbers + control_num)
    if validation_control_num == 0:
        print("ok")
        return True
    else:
        print("nie ok :(")
        return False


def handle_creating_control_num():
    try:
        control_num = create_luhn_number(e1.get())
        messagebox.showinfo("Cyfra kontrolna", "Wygenerowany ciąg z cyfrą kontrolną to:\n" + str(control_num))
    except Exception as e:
        messagebox.showinfo("Błąd w walidacji PESEL", 'Błąd walidacji: ' + str(e))


def handle_validation_of_control_num():
    try:
        valid_control_num = validate_control_number(e2.get())
        if valid_control_num:
            succes_msg = "Cyfra kontrolna jest poprawna"
            messagebox.showinfo("OK", succes_msg)
        else:
            fail_msg = "Cyfra kontrolna jest niepoprawna!"
            messagebox.showinfo("Niepoprawna cyfra kontrolna", fail_msg)
    except Exception as e:
        messagebox.showinfo("Błąd", 'Błąd walidacji cyfry kontrolnej: ' + str(e))


if __name__ == '__main__':
    master = Tk()
    master.title("Algorytm-Luhna")
    master.geometry("500x150")

    Label(master, text="podaj ciąg znaków do wygenerowania cyfry kontrolnej").grid(row=0)
    e1 = Entry(master)
    e1.grid(row=0, column=1)
    Button(master, text='generuj cyfre kontrolną', command=handle_creating_control_num).grid(row=3, column=1, sticky=W, pady=4)

    Label(master, text="podaj ciąg znaków z cyfrą kontrolną po myślniku do walidacji").grid(row=4)
    e2 = Entry(master)
    e2.grid(row=4, column=1)
    Button(master, text='generuj cyfre kontrolną', command=handle_validation_of_control_num).grid(row=5, column=1, sticky=W,
                                                                                             pady=4)
    mainloop()
