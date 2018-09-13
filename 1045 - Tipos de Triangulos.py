# 1045 - Tipos de Triangulos

'''
1. Ler 3 float's
2. Ordenar as entradas em ordem decrescente
3. Definir qual o tipo de triangulo os tres lados formam
'''

# Entrada
a, b, c = map(float, input().split())

# Ordenamento
if a < b:
    aux = a
    a = b
    b = aux
if b < c:
    aux = b
    b = c
    c = aux
if c > b:
    aux = c
    c = b
    b = aux
if b > a:
    aux = b
    b = a
    a = aux

# Saida
if a >= b+c:
    print('NAO FORMA TRIANGULO')
elif a**2 == b**2+c**2:
    print('TRIANGULO RETANGULO')
elif a**2 > b**2+c**2:
    print('TRIANGULO OBTUSANGULO')
elif a**2 < b**2+c**2:
    print('TRIANGULO ACUTANGULO')
if a==b==c:
    print('TRIANGULO EQUILATERO')
elif a==b or a==c or b==c:
    print('TRIANGULO ISOSCELES')
