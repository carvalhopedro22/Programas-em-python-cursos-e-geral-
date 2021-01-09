lista = []
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0: #se for o primeiro elemento
        lista.append(n)
    elif n > lista[-1]: #maior que o ultimo elemento
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista): #0 ate a ultima posicao
                if n <= lista[pos]:
                    lista.insert(pos, n)
                    break
                pos = pos + 1
print(lista)