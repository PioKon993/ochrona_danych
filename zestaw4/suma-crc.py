from tkinter import *
from tkinter import messagebox


def validate_pesel(pesel):
    check_pesel_length(pesel)
    check_pesel_is_number(pesel)

    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    control_sum = 0
    i = 0
    for weight in weights:
        control_num = weight * int(pesel[i:i + 1])
        if control_sum > 9:
            control_sum = control_sum % 10
        control_sum += control_num
        i += 1

    if control_sum > 9:
        control_sum = control_sum % 10

    result_number = 10 - control_sum
    last_num_in_pesel = int(pesel[10])
    if result_number == last_num_in_pesel:
        return True
    else:
        return False


def check_pesel_is_number(pesel):
    try:
        int(pesel)
    except ValueError:
        raise ValueError("podany pesel zawiera niepoprawne znaki")


def check_pesel_length(pesel):
    if len(pesel) != 11:
        raise ValueError('wprowadzony PESEL nie ma dokładnie 11 cyfr')


def handle_pesel_validation():
    try:
        valid_control_num = validate_pesel(e1.get())
        if valid_control_num:
            succes_msg = "PESEL o numerze " + e1.get() + " jest poprawny"
            messagebox.showinfo("OK", succes_msg)
        else:
            fail_msg = "PESEL o numerze " + e1.get() + " jest niepoprawny! Cyfra kontrolna się nie zgadza."
            messagebox.showinfo("Błąd w walidacji PESEL", fail_msg)
    except Exception as e:
        messagebox.showinfo("Błąd w walidacji PESEL", 'Błąd walidacji: ' + str(e))


if __name__ == '__main__':
    master = Tk()
    master.title("walidacja PESELU")
    master.geometry("300x100")

    Label(master, text="wprowadź PESEL").grid(row=0)
    e1 = Entry(master)
    e1.grid(row=0, column=1)
    Button(master, text='waliduj PESEL', command=handle_pesel_validation).grid(row=3, column=1, sticky=W, pady=4)

    mainloop()
