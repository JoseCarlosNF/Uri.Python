# -*- coding: utf-8 -*-
# 1958 - Notação Científica

# Procedimento
def notacaoCientifica(entrada):

    contador = 0

    # Sinal do Numero/Transfomar em positivo
    if entrada > 0:
        sinal = '+'
    else:
        entrada *= -1
        sinal = '-'

    # Operações
    if 0 <= entrada < 1:
        op = 1
        while entrada < 1:
            entrada *= 10
            contador += 1

    elif 1 <= entrada <= 10:
        op = 2
        pass

    elif entrada > 10:
        op = 2
        while entrada > 10:
            entrada /= 10
            contador += 1

    # Sinal Contador
    if op == 1:
        sinalContador = '-'
    elif op == 2:
        sinalContador = '+'

    print('{}{:.4f}'.format(sinal, entrada), end='')
    print('E', end='')
    print('{}{:0>2}'.format(sinalContador, contador))


# Main
entrada = float(input())
notacaoCientifica(entrada)
