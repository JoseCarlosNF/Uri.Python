# -*- coding: utf-8 -*-
# 1161 - Soma de Fatoriais


def fatorial(n):
    if n == 0:
        return 1
    else:
        return n*fatorial(n-1)


while (True):
    try:
        a, b = map(int, input().split())
        soma = fatorial(a) + fatorial(b)
        print(soma)
    except EOFError:
        break
