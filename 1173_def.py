# coding: utf-8 -*-
# 1173 - Preenchimento de Vetor I


# Função
def vetor_dobro(entrada):
    vetor = [entrada]
    for i in range(9):
        vetor.append(vetor[i] * 2)
    return vetor


# Procedimento
def imprimir_vetor(vetor):
    for i in range(len(vetor)):
        print('N[%d] = %d' % (i, vetor[i]))


# Main
vetor = vetor_dobro(int(input()))
imprimir_vetor(vetor)
