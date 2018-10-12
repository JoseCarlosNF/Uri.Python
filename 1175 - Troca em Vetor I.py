# 1175 - Troca em Vetor I

vetor = []

for i in range(20):
    vetor.append(int(input()))

i = 0
j = 19
while i < j:
    aux = vetor[i]
    vetor[i] = vetor[j]
    vetor[j] = aux
    i += 1
    j -= 1

for i in range(20):
    print('N[%d] = %d' % (i, vetor[i]))