# 1180 - Menor e Posicao

# Tamanho do vetor
tamVetor = int(input())

# Entrda dos valores do vetor
vetor = list(map(int, input().split()))
'''
for i in range(tamVetor):
    # Primeiro caso
    if i==0:
        menor = vetor[i]

    # Casos seguintes
    if vetor[i] < menor:
        menor = vetor[i]
        posicao = i
'''
print("Menor valor: %d" % min(vetor))  # menor
print("Posicao: %d" % vetor.index(min(vetor)))  # posicao
