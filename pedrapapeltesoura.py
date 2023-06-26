import random

user_point = 0
computer_point = 0
options = [
    'R',
    'T',
    'P'
]

while True:
    user_choice = input(
        'escolha um R(pedra)/T(tesoura)/P(papel)ou Q para sair.').upper()

    if user_choice == 'Q':
        break

    if user_choice not in options:
        continue

    choice_computer = random.randint(0, 2)

    computer_option = options[choice_computer]

    print('o computador escolheu:' + computer_option)

    if user_choice == computer_option:
        print('empate')

    elif user_choice == 'R' and computer_option == 'T':
        print('Vc ganhou')
        user_point = user_point + 1

    elif user_choice == 'T' and computer_option == 'P':
        print('Vc ganhou')
        user_point = user_point + 1

    elif user_choice == 'P' and computer_option == 'R':
        print('Vc ganhou')
        user_point = user_point + 1
    else:
        print("Você perdeu!")


print('sua pontuaçao: ' + str(user_point))
print('pontuaçao pc: ' + str(computer_point))


if computer_point > user_point:
    print('DERROTA')
elif user_point == computer_point:
    print('EMPATE')
else:
    print('VITORIA')
