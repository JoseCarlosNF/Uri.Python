# 1078 - Tabuada

'''
1. Ler 1 inteiro (N)
2. Mostra a tabuada de N
'''

multi = 1

# Entrada
N = int(input())

# Tabuada / Saida
while multi < 11:
    resul = multi * N
    print("%d x %d = %d" % (multi, N, resul))
    multi += 1
