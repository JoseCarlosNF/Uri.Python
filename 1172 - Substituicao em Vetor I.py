# 1172 - Substituicao em Vetor

vetor = []

for i in range(10):

    # Entrada
    aux = int(input())
    vetor.append(aux)

    # Condicao para indice i receber 0
    if vetor[i] <= 0:
        vetor[i] = 1

for i in range(0, 10):
    print("X[%d] = %d" % (i, vetor[i]))
