peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = (peso/(altura*altura))
print('O imc da pessoa é: {:.2f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >= 30 and imc < 40:
    print('Obesidade')
elif imc > 40:
    print('Obesidade morbida')