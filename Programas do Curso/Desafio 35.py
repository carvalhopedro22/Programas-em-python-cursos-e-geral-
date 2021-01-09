a = int(input('Digite o primeiro segmento '))
b = int(input('Digite o segundo segmento: '))
c = int(input('Digite o terceiro segmento '))
if  (b - c) < a < (b + c) and (a - c)  < b < (a + c) and (a - b) < c < (a + b):
  print('Formam um triangulo')
else:
  print('Nao formam um triangulo')