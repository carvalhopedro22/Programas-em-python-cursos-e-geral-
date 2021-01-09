dist = int(input('Qual a distancia em km da sua viagem? '))
if dist <= 200:
  preco = dist * 0.5
  print('O preço da viagem sera de: {}'.format(preco))
else:
  preco = dist * 0.45
  print('O preço da viagem sera de: {}'.format(preco))