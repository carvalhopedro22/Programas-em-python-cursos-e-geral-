salario = int(input('Digite o salario '))
if salario > 1250:
  novosalario = (salario + (10/100) * salario)
  print('Seu novo salario é {}'.format(novosalario))
else:
  novosalario = (salario + (15/100) * salario)
  print('Seu novo salario é {}'.format(novosalario))