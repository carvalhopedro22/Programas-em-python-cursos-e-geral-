n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opçao = 0
while opçao != 5:

    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair do programa''')

    opçao = int(input('>>>>>>>>>> Qual sua opção? '))

    if opçao == 1:
        soma = n1 + n2
        print('A soma de {} e {} é {}'.format(n1,n2,soma))
    elif opçao == 2:
        produto = n1 * n2
        print('O produto de {} e {} é {}'.format(n1,n2,produto))
    elif opçao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior é {}'.format(n1,n2,maior))
    elif opçao == 4:
        print('Informe os numeros novamente')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opçao == 5:
        print('Finalizando..')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
print('Fim do programa')