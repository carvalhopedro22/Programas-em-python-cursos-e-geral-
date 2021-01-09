import random
nome = input('Digite o primeiro nome: ')
nome2 = input('Digite o segundo nome: ')
nome3 = input('Digite o terceiro nome: ')
nome4 = input('Digite o quarto nome: ')
lista = [nome,nome2,nome3,nome4]
random.shuffle(lista)
print('Ordem de apresentação:')
print(lista)