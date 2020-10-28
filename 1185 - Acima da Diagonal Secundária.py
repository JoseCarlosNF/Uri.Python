# QUESTÃO 02 - LISTA 04
# codificar somatorio da Diagonal secundaria de uma matriz
# 1. receber os valores da matriz
# 2. somar elementos acima da Diagonal secundaria

soma = 0
for linha in range(12):
    for coluna in range(12):
        entrada = int(input())
        if 0 <= (linha + coluna) <= 10:
            soma += entrada
print(f'Soma acima diagonal secundaria: {soma}')
