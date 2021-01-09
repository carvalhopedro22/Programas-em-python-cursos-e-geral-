num = int(input('Insira um numero inteiro: '))
print('''Escolha uma das conversões:
[1] converter para BINARIO 
[2] converter para OCTAL 
[3] converter para HEXADECIMAL\n''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para binario é igual a {}'.format(num,bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para octal é igual a {}'.format(num,oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num,hex(num)[2:]))
else:
    print('Opcao invalida')