a = int(input('Digite o primeiro segmento '))
b = int(input('Digite o segundo segmento: '))
c = int(input('Digite o terceiro segmento '))
if  (b - c) < a < (b + c) and (a - c)  < b < (a + c) and (a - b) < c < (a + b):
  print('Formam um triangulo')
  if a == b == c:
      print('Triangulo equilatero')
  elif a == b != c or a == c != b or b == c != a:
      print('Triangulo isosceles')
  else:
      print('Triangulo escaleno')
else:
    print('Nao existe triangulo nessas condições')