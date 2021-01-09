somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for c in range(1,5):
    print('-----{} PESSOA -----'.format(c))
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo[M/F]: '))
    somaidade = somaidade + idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade > 20:
        totmulher20 = totmulher20 + 1
mediaidade = somaidade / 4
print('A media das idades é {}'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem,nomevelho))
print('Ao todo sao {} mulheres com menos de 20 anos'.format(totmulher20))