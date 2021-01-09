soma = 0
contpar = 0
for c in range(1,7):
    n = int(input('Digite os numeros: '))
    if n % 2 == 0:
        soma = soma + n
        contpar = contpar + 1
print('A soma dos pares vale {} e a quantidade de numeros pares é {}'.format(soma,contpar))