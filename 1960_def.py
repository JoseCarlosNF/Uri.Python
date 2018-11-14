# -*- coding: utf-8 -*-
# 1960 - Numeração Romana para Numeros de Pagina


def separacao(entrada):
    if 100 <= entrada:
        centena = entrada // 100
        dezena = (entrada % 100) // 10
        unidade = (entrada % 10) % 10
        return centena, dezena, unidade

    elif 10 <= entrada < 100:
        dezena = entrada // 10
        unidade = entrada % 10
        return dezena, unidade

    elif 0 < entrada < 10:
        unidade = list()
        unidade.append(entrada)
        return unidade


def centena(entrada):

    if entrada == 1:
        saida = 'C'
    elif entrada == 2:
        saida = 'CC'
    elif entrada == 3:
        saida = 'CCC'
    elif entrada == 4:
        saida = 'CD'
    elif entrada == 5:
        saida = 'D'
    elif entrada == 6:
        saida = 'DC'
    elif entrada == 7:
        saida = 'DCC'
    elif entrada == 8:
        saida = 'DCCC'
    elif entrada == 9:
        saida = 'CM'

    return saida


def dezena(entrada):
    if entrada == 0:
        saida = ''
    elif entrada == 1:
        saida = 'X'
    elif entrada == 2:
        saida = 'XX'
    elif entrada == 3:
        saida = 'XXX'
    elif entrada == 4:
        saida = 'XL'
    elif entrada == 5:
        saida = 'L'
    elif entrada == 6:
        saida = 'LX'
    elif entrada == 7:
        saida = 'LXX'
    elif entrada == 8:
        saida = 'LXXX'
    elif entrada == 9:
        saida = 'XC'

    return saida


def unidade(entrada):

    if entrada == 0:
        saida = ''
    elif entrada == 1:
        saida = 'I'
    elif entrada == 2:
        saida = 'II'
    elif entrada == 3:
        saida = 'III'
    elif entrada == 4:
        saida = 'IV'
    elif entrada == 5:
        saida = 'V'
    elif entrada == 6:
        saida = 'VI'
    elif entrada == 7:
        saida = 'VII'
    elif entrada == 8:
        saida = 'VIII'
    elif entrada == 9:
        saida = 'IX'

    return saida


x = int(input())

saida = separacao(x)

# Números de até três casas
if len(saida) == 3:
    print(centena(saida[0]), end='')
    print(dezena(saida[1]), end='')
    print(unidade(saida[2]))

# Números de até duas casas
elif len(saida) == 2:
    print(dezena(saida[0]), end='')
    print(unidade(saida[1]))

# Números com apenas uma casa
elif len(saida) == 1:
    print(unidade(saida[0]))
