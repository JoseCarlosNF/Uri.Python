# -*- coding: utf-8 -*-
# 1170 - Blobs

c = list()
qtd_testes = int(input())

for i in range(qtd_testes):
    c.append(float(input()))

for i in range(qtd_testes):
    dias = 0
    while c[i] > 1:
        c[i] -= c[i] * 0.5
        dias += 1
    print('%d dias' % dias)
