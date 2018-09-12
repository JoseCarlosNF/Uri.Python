import math

valor1 = input().split(" ")
valor2 = input().split(" ")
x1, y1 = valor1
x2, y2 = valor2

distancia = math.sqrt((float(x2)-float(x1))**2 + (float(y2)-float(y1))**2) 

print('%.4f' % distancia)