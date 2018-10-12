# 1177 - Preenchimento de Vetor II

# T-1 = valor maximo do vetor
T = int(input())

# Criar vetor vazio
N = []

aux = 0

# Adicionar itens ao vetor conforme regra
for i in range(1000):
    N.append(aux)
    aux += 1
    if aux == T:
        aux = 0

    # Saida
    print('N[%d] = %d' % (i, N[i]))