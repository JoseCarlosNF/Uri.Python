# 1174 - Selecao em Vetor I

A = []
# Inserção dos valores no vetor
for i in range(100):
    A.append(float(input()))

# Imprimir caso o conteudo do indice i seja <= 100
for i in range(100):
    if A[i] <= 10:
        print("A[%d] = %.1f" % (i, A[i]))
