from random import randint
itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
print('O computador escolheu {}'.format(itens[computador]))
print('''Suas opções:
[0] pedra 
[1] papel 
[2] tesoura''')
print('-=' *10)
jogador = int(input('Qual sua jogada? '))
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' *10)
if computador == 0: #pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('INVALIDO')
elif computador == 1: #papel
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('INVALIDO')
elif computador == 2: #tesoura
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('INVALIDO')