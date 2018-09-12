# 1036 - Fórmula de Bhaskara

'''
1.Ler 3 pontos flutuantes

2.Se não for possivel calcular a raiz mostrar, "Impossivel calcular"
    Divisão por zero ou raiz negativa

3. Imprimir o resultado com 5 digitos de flutuação
'''

import math
valores = input().split(" ")

a, b, c = valores
a = float(a)
b = float(b)
c = float(c)

x = (b ** 2) - (4 * a * c)

if a == 0 or x < 0:
    print('Impossivel calcular')

elif a != 0 and x >= 0:
    x = math.sqrt(x)

    r1 = (-b+x) / (2*a)
    r2 = (-b-x) / (2*a)

    print('R1 = %.5f' % r1)
    print('R2 = %.5f' % r2)
