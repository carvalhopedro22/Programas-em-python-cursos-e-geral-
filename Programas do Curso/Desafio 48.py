soma = 0
cont = 0
for c in range(1,501,2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1 #conta quantos numeros vão ser divisíveis por 3
print('A soma é {} e a quantidade de numeros que foram somados é {}'.format(soma,cont))