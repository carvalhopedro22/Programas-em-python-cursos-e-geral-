from random import randint
computador = randint(0,5)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar')
print('-=-'*20)
jogador = int(input('Em que numero pensei? '))#jogador tenta adivinhar
if jogador == computador:
  print('Parabens, me venceu')
else:
  print('Ganhei, eu pensei no {} e nao no {}'.format(computador,jogador))