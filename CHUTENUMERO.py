import random

print('seja bem vindo')
numero = input('digite um numero teto: ')

if numero.isdigit():
    numero = int(numero)
else:
    print('erro digite um numero')
    quit()

randonnumero = random.randint(0, numero)

acertos = 0

while True:
    digitousuario = input('advinhe o numero: ')

    if digitousuario.isdigit():
        digitousuario = int(digitousuario)
    else:
        print('ERRO valor informado nao e numerico!!!')
        continue
    acertos = acertos+1
    if digitousuario == numero:
        print('acertou')
        break
    elif digitousuario > numero:
        print('o numero e menor q isso')
    else:
        print('o numero e maior q isso')

print('tentativas: ' + str(acertos))
