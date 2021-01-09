frase = input('Digite uma frase: ').upper()
print('A letra "A" apareceu {} vezes'.format(frase.count('A')))
print('A letra "A" apareceu na primeira vez no indice {}'.format(frase.find('A')))
print('A letra "A" apareceu na ultima vez no indice {}'.format(frase.rfind('A')))