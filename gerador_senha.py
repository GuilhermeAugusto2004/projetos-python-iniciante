import random
import string


def password_generator(len_pass=8):
    ascii_option = string.ascii_letters
    number_option = string.digits
    punt_option = string.punctuation
    option = ascii_option + number_option + punt_option

    password_user = ""

    for i in range(0, len_pass):
        digit = random.choice(option)
        password_user = password_user + digit

    return password_user


choice_user = input("Quantos digitos na senha?")

if choice_user.isdigit():
    choice_user = int(choice_user)
else:
    print("Entrada invalida!")
    quit()

resonse = password_generator(len_pass=choice_user)
print(f"Senha Gerada:\n{resonse}")
