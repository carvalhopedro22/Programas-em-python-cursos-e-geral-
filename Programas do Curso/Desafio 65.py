num = 0
cont = 0
soma = 0
num = int(input('Digite um numero '))
while num != 999:
    soma = soma + num
    cont = cont + 1
    num = int(input('Digite um numero '))
print('Você digitou {} numeros e a soma foi de {}'.format(cont,soma))