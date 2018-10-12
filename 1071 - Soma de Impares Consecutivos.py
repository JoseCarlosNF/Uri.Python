# 1071 - Soma de Impares Consecutivos

'''
1. Ler 2 valores inteiros (x,y)
2. Calcular a soma dos numeros impares entre eles
'''
soma = 0
# Entrada
x = int(input())
y = int(input())

# Logica
if x > y:
    x -= 1
    while x > y:
        if x % 2 != 0:
            soma += x
        x -= 1

if y > x:
    y -= 1
    while y > x:
        if y % 2 != 0:
            soma += y
        y -= 1

# Saida
print("%d" % soma)
