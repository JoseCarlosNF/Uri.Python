# -*- conding: utf-8 -*-
# 1329 - Cara ou Coroa
while (True):
    maria = 0
    joao = 0

    qtd_teste = int(input())

    if qtd_teste == 0:
        break
    else:
        lista = list(map(int, input().split()))
        
        for i in lista:
            if i == 0:
                maria += 1
            else:
                joao += 1
        print('Mary won %d times and John won %d times' % (maria, joao))
