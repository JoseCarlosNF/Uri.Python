# 1072 - Intervalo 2

'''
1. Ler 1 valor inteiro (quantidade de valores que serão lidos)
2. Mostrar desses valores quais estão dentro do intervalo 10,20 e quantos fora
'''

dentro = 0
fora = 0

# Entrada
N = int(input())

while N > 0:
    valor = int(input())
    if 10 <= valor <= 20:
        dentro += 1
    else:
        fora += 1
    N -= 1

# Saida
print("{} in".format(dentro))
print("{} out".format(fora))
