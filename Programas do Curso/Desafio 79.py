lista = []
maior = menor = 0
for c in range(0,5):
    lista.append(int(input('Digite os valores da lista: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print(f'A lista é formada por {lista}')

print(f'O maior foi {maior}')
print(f'O menor foi {menor}')