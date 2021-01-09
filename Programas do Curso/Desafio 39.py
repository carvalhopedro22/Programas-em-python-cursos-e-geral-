idade = int(input('Digite sua idade: '))
if idade < 18:
    falta = 18 - idade
    print('Ainda tera que se alistar. Falta(am) {} anos'.format(falta))
elif idade == 18:
    print('Está na hora de se alistar')
else:
    passou = idade - 18
    print('Ja passou da hora de se alistar. Passaram(ou) {} anos desde que voce deveria ter se alistado'.format(passou))