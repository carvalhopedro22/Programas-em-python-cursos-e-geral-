n = 0
soma = 0
qtd = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    soma = soma + n
    qtd = qtd + 1
print('A soma foi {} e a quantidade de numeros foi {}'.format(soma,qtd))