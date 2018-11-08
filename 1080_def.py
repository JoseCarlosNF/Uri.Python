# -*- coding: utf-8 -*-
# 1080 - Maior e Posição


# Função (retorna o vetor inserido)
def vetor(tamVetor):
    vetor = list()
    for i in range(tamVetor):
        vetor.append(int(input()))
    return vetor


# Função (retorna o maior valor do vetor)
def maior(vetor):
    for i in range(len(vetor)):
        if i == 0:
            maior = vetor[i]
        else:
            if vetor[i] > maior:
                maior = vetor[i]
    return maior


# Função (retorna a posição do maior valor no vetor)
def posicao(vetor, maior):
    posicao = vetor.index(maior) + 1    # Posição deve começar em 1, ao invés de 0.
    return posicao


# Main
vetor = vetor(100)
maior = maior(vetor)
posicao = posicao(vetor, maior)
print('%d' % maior)
print('%d' % posicao)