from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(1,11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou impar?[P/I]? ')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o computador {computador}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
           print('Voce venceu')
           v = v + 1
        else:
            print('Voce perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
           print('Voce venceu')
           v = v + 1
        else:
            print('Voce perdeu')
            break
    print('Vamos jogar novamente')
print(f'Voce venceu {v} vezes')