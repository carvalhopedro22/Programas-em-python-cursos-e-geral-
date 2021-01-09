a1 = int(input('Qual o primeiro termo? '))
r = int(input('Qual a razão da progressão? '))
for c in range(a1, 10*r ,r):
    print('{}'.format(c), end = '->')
print('FIM')