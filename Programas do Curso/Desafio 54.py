from datetime import date
atual = date.today().year
contmenor = 0
contmaior = 0
for c in range(0,7):
    ano = int(input('Em que ano você nasceu? '))
    idade = atual - ano
    if idade < 18:
        print('É maiores')
        contmenor = contmenor + 1
    else:
        print('É maiores')
        contmaior = contmaior + 1
print('A quantidade de menores é {} e de maiores é {}'.format(contmenor,contmaior))