# -*- coding: utf-8 -*-
# 1172 - Substituição em Vetor I


# Função
def função(entrada):
    if entrada <= 0:
        saida = 1
    else:
        saida = entrada
    return saida


# Main
lista = list()

for i in range(10):
    entrada = int(input())
    lista.append(função(entrada))
    print('X[{}] = {}'.format(i, lista[i]))
