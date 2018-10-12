# 1176 - Fibonacci em Vetor

# Numero de casos a serem analisados
nCasos = int(input())

for i in range(nCasos):
    # Entrada da posição a ser obtida
    valor = int(input())

    # vetor inicial
    vetor = [0,1]

    # Logica
    i = 1
    while i < valor:
        vetor.append(vetor[i]+vetor[i-1])
        i += 1
    # Saida
    print('Fib(%d) = %d' % (valor, vetor[valor]))