# 1070 - Seis Números Ímpares

'''
1. Ler 1 valor inteiro
2. Apresentar 6 valores ímpares consecutivos
'''

contador = 0

# Entrada
x = int(input())

# Logica
while contador < 12:
    if x % 2 != 0:
        print(x)
    contador += 1
    x += 1
