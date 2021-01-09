sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dado invalido. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado'.format(sexo))