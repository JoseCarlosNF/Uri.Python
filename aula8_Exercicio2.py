# -*- coding: utf-8 -*-
# Aula 8 - Exercicio 2


def multi(n1, n2):
    if n1 == 0:
        return 0
    else:
        return multi(n1-1, n2) + n2


# Main
x = int(input('Num1: '))
y = int(input('Num2: '))

print(multi(x, y))
