# 1173 - Preenchimento de Vetor I

# Criação da lista e inserção do 1º componente
N = [int(input())]

# Inserção dos demais componentes
for i in range(9):
    aux = N[i] * 2
    N.append(aux)

# Saida
for i in range(10):
    print("N[%d] = %d" % (i, N[i]))