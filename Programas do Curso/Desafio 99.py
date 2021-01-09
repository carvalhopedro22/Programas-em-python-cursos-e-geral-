def maior(* num):
    cont = maior = 0
    print('\nAnalisando os valores:')
    for valor in num:
        print(f'{valor}',end = '')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nQuantidade de valores{cont}')
    print(f'O maior valor foi {maior}')

maior(2,8,7,6,5,4)