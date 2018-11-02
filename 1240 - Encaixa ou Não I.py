# -*- coding: utf-8 -*-
# 1240 - Encaixa ou Não I

qtd_teste = int(input())

for i in range(qtd_teste):
    num1, num2 = input().split()

    # Se os ultimos numeros de 'num1' foram iguais aos numeros componentes de 'num2'
    if num2 == num1[len(num1)-len(num2):len(num1)]:
        print('encaixa')
    else:
        print('nao encaixa')
