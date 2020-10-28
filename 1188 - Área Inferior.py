# QUESTÃO 06 - LISTA 04
# codificar somatorio da área inferior de uma matriz
# 1. receber os valores da matriz
# 2. somar elementos da área inferior

soma = 0
cont = 0
for linha in range(12):
  for coluna in range(12):
    entrada = int(input())
    if(linha >= 7 and linha + coluna >= 12 and coluna < linha):
      soma += entrada
      cont += 1
print(f'Soma da área inferior: {soma}')
