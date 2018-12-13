def rsa_encoding(a, w, n):
    # Funkcja oblicza modulo potęgę podanej liczby
    #
    # wykładnik w rozbieramy na sumę potęg 2. Dla reszt
    # niezerowych tworzymy iloczyn potęg a modulo n.
    pot = a
    result = 1
    q = w
    while q:
        if (q % 2) == 1:
            result = (result * pot) % n
        pot = (pot * pot) % n
        q //= 2
    return result


def text_encoding(text_to_encode):
    with open('public.key') as file:
        e = int(file.readline())
        n = int(file.readline())

    text_to_encode = add_zeros_if_odd_length(text_to_encode)

    result = ''
    i = 0
    while i < len(text_to_encode) - 1:
        letters_to_encode = create_ascii_code_from_two_letters(i, text_to_encode)
        result = result + str(rsa_encoding(letters_to_encode, e, n)) + ","
        i += 2
    result = remove_last_char(result)

    save_encoded_text_to_file(result)


def save_encoded_text_to_file(result):
    with open('text.enc', 'w+') as file:
        file.write(result)


def remove_last_char(result):
    result = result[:-1]
    return result


def create_ascii_code_from_two_letters(i, text_to_encode):
    first_string = str(ord(text_to_encode[i])).zfill(3)
    second_string = str(ord(text_to_encode[i + 1])).zfill(3)
    number_to_encode = int(first_string + second_string)
    return number_to_encode


def add_zeros_if_odd_length(text_to_encode):
    if len(text_to_encode) % 2 == 1:
        text_to_encode += chr(0)
    return text_to_encode


def text_decoding():
    with open('private.key') as file:
        d = int(file.readline())
        n = int(file.readline())

    with open('text.enc') as file:
        secret_text = file.read()
    secret_numbers = secret_text.split(",")

    result = ''
    for number_to_decode in secret_numbers:
        two_ascii_letters = str(rsa_encoding(int(number_to_decode), d, n))
        first_ascii_letter = int(two_ascii_letters[0:-3])
        second_ascii_letter = int(two_ascii_letters[-3:])
        result += chr(first_ascii_letter) + chr(second_ascii_letter)
    return result

if __name__ == '__main__':
    with open('text.txt') as f:
        text_to_encode = f.read()

##    print("tekst do zaszyfrowania: ")
##    print(text_to_encode)
##
##    text_encoding(text_to_encode)
##
##    decoded_text = text_decoding()
##    print("odkodowany tekst: " + decoded_text)


