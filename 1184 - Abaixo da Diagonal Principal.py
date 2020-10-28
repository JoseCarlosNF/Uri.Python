# QUESTÃO 05 - LISTA 04
# codificar somatorio da Diagonal Principal de uma matriz
# 1. receber os valores da matriz
# 2. somar elementos abaixo da Diagonal Principal

soma = 0
for linha in range(12):
    for coluna in range(12):
        entrada = int(input())
        if (coluna < linha):
            soma += entrada
print(f'Soma abaixo diagonal principal: {soma}')
