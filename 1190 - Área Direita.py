# QUESTÃO 04 - LISTA 04
# codificar somatorio da área direita de uma matriz
# 1. receber os valores da matriz
# 2. somar elementos da área direita

soma = 0
cont = 0
for linha in range(12):
  for coluna in range(12):
    entrada = int(input())
    if(linha + coluna >= 12 and coluna - linha >= 1):
      soma += entrada
      cont += 1
print(f'Soma da área direita: {soma}')
