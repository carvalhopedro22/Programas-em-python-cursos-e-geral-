tot = 0
totmil = 0
menor = 0
cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    cont = cont + 1
    tot = tot + preço
    if preço > 1000:
        totmil = totmil + 1
    if cont == 1:
        menor = preço
    else:
        if preço < menor:
            menor = preço
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Continuar?[S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('Fim do programa')
print(f'Total foi de R${tot}')
print(f'Temo {totmil} produtos custando mais de R$1000')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')