# 1043 - Triangulo

'''
1. Ler 3 float's
2. Verificar se os valores formam um triangulo
    2.1 Se não calcular a area do trapezio de bases A e B, de altura C
    2.2 Imprimir 'Area = xx.x'
3. Calcular o perimetro do triangulo
4. Imprimir 'Perimetro = xx.x'
'''

# Entrada
a, b, c = map(float, input().split())

# Verificação do triangulo
if ((a<(b+c)) and (b<(a+c)) and (c<(a+b))):
    perimetroTriangulo = a + b + c
    print('Perimetro = %.1f' % perimetroTriangulo)
else:
    areaTrapezio = c * (a + b) / 2
    print('Area = %.1f' % areaTrapezio)
