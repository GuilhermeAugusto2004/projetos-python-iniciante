import json
import random

f = open("words.json", encoding="utf8")

words = json.load(f)
choice_c = random.choice(list(words))

print("Ola seja Bem Vindo")
print("###########################")

n_choises = 5
win = False

while n_choises > 0 and win is not True:
    print("DICA: " + words[choice_c])
    answer_user = input("DATA:  DDMMAAAA\n")
    print("#################\n")

    if len(answer_user) != 8:
        print("ERRO NA ENTRADA. A RESPOSTA DEVE CONTER 8 DIGITOS.")
        continue

    if answer_user.isdigit():
        check = []
        pontuation = 0
        for i in range(8):
            if answer_user[i] == choice_c[i]:
                check.append("acertou")
                pontuation = pontuation + 1
            else:
                check.append("errou")

        print("Resposta: \n")
        print("|".join(check))
        print(" |".join(answer_user))
        print("######################\n")

        if pontuation == 8:
            win = True
    else:
        print("A RESPOSTA DEVE SER UMA DATA!")
        continue

    n_choises = n_choises - 1

if win:
    print("VITORIA!!!!")
else:
    print("DERROTA")
    print("A resposta era: " + choice_c)
