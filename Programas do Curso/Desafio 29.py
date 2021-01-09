vel = int(input('Qual a velocidade do carro? '))
if vel > 80:
  print('Você ganhou multa')
  multa = (vel - 80) * 7
  print('Sua multa foi de {}'.format(multa))
print('Siga feliz')