casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salario? '))
qtdanos = int(input('Em quantos anos fará o pagamento? '))
prestacao = casa/(qtdanos * 12)
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa,qtdanos,prestacao))


if prestacao > ((30/100)*salario):
    print('Emprestimo nao concedido')
else:
    print('Emprestimo concedido')