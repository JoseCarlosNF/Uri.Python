# QUESTÃO 03 - LISTA 04
# codificar somatorio da área superior de uma matriz
# 1. receber os valores da matriz
# 2. somar elementos da área superior

soma = 0
cont = 0 
for linha in range(12):
  for coluna in range(12):
    entrada = int(input())
    if (coluna - linha >= 1 and coluna + linha <= 10):
      soma += entrada
      cont += 1
      if linha == 5:
        break
print(f'Soma da área superior: {soma}')
