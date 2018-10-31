# -*- coding: utf-8 -*-
# 1169 - Trigo no Tabuleiro


qtd_testes = int(input())

for i in range(qtd_testes):
    casas_no_tabuleiro = int(input())
    qtd_de_graos = 1

    for i in range(casas_no_tabuleiro):
        qtd_de_graos *= 2

    kg = (qtd_de_graos/12)/1000

    print('%d kg' % kg)
