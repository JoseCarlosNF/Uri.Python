# QUESTÃO 07 - LISTA 04
# codificar somatorio da área esquerda de uma matriz
# 1. receber os valores da matriz
# 2. somar elementos da área esquerda

soma = 0
cont = 0
for linha in range(12):
  for coluna in range(12):
    valor = float(input())
    if(linha - coluna >= 1 and linha + coluna <= 10):
      soma += valor
      cont += 1
print(f'Soma da área esquerda: {soma}')
