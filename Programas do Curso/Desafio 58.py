from random import randint
computador = randint(0,10)
print('Sou seu computador... Acabei de pensar em um numero entre 0 e 10')
print('Será que você consegue adivinhar?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpite = palpite + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente novamente')
        elif jogador > computador:
            print('Menos... Tente novamente')
print('Acertou com {} tentativas'.format(palpite))

print('''[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa''')