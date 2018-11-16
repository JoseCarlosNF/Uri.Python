# -*- coding: utf-8 -*-
# Aula 8 - Exercicio 4


# Fatorial
def fact(n):
    if n == 0:
        return 1
    else:
        return fact(n-1)*n


# Super Fatorial
def superFatorial(n):
    total = 1
    for i in range(1, n+1):
        total *= fact(i)
    return total

n = int(input('Num (superfatorial): '))
print(superFatorial(n))