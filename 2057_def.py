# -*- coding: utf-8 -*-
# 2057 - Fuso Horario


# Procedimento
def fusoHorario(saida, duracao, fuso):

    if saida == 0:
        saida = 24

    hora = saida + duracao + fuso

    if hora == 24:
        hora = 0
    elif hora > 24:
        hora -= 24
        
    print(hora)


# Main
saida, duracao, fuso = map(int, input().split())

fusoHorario(saida, duracao, fuso)
