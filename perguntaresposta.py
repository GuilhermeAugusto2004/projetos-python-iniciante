print('seja bem vindo!')
entrada = input('vc deseja jogar?')

if entrada != 'S' 'SIM' == 'S' 's' == 'S':
    quit()

pontos = 0

print('começando')
print("sua mae e minha? \n (A)sim \n (B)nao \n (C)talvez")
resposta1 = input('Resposta:')

if resposta1 == 'A':
    print('correto!')
    pontos = pontos + 1

else:
    print('incorreto!')

print("AAA? \n (A)BBB \n (B)AAA \n (C)CCC")
resposta1 = input('Resposta:')

if resposta1 == 'B':
    print('correto!')
    pontos = pontos + 1

else:
    print('incorreto!')

print(f'obrigado, pontuaçao: {pontos}')
