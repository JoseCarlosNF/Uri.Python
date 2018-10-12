# 1187 - Area Superior

soma = 0.0

# Numero de linhas e colunas da Matriz
n_linhas = 12
n_colunas = 12

# Entrada da Operação
operacao = input().upper()

# criar matriz
matriz = []

# cria a linha i
for l in range(n_linhas):
    linha = []

    # adiciona a coluna j, dentro da linha i
    for c in range(n_colunas):
        # entrada dos Valores na Matriz
        linha.append(float(input()))

    # a linha é adicionada a matriz
    matriz.append(linha)

# Condição da Area Superior
l=0
while l<=4:
    c=l+1
    while c<=10-l:
        soma += matriz[l][c]
        c += 1
    l += 1

# Saida
if operacao == 'S':
    print('%.1f' % soma)
elif operacao == 'M':
    print('%.1f' % (soma / 30.0))
