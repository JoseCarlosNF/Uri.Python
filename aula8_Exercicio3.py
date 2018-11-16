# -*- coding: utf-8 -*-
# Aula 8 - Exercicio 3


def imprime(string):
    x = len(string)
    print('~'*x)
    print('%s' % string)
    print('~'*x)


# Imprime números naturais de 0 até N em ordem decrescente
def decrescente(n):
    print(n)
    if n == 0:
        return 0
    else:
        return decrescente(n-1)


# Imprime números pares de 0 até N em ordem decrescente
def paresDecrescente(n):
    if n % 2 == 0:
        print(n)
    if n == 0:
        return 0
    else:
        return paresDecrescente(n-1)


# Imprime números pares de 0 até N em ordem crescente
def paresCrescente(n, i=0):
    if i % 2 == 0:
        print(i)
    if n > i:
        paresCrescente(n, i+1)
    else:
        return 0


''' Main '''
num = int(input('Num: '))

imprime('Numeros decrescntes de 0 até %d' % num)
decrescente(num)

imprime('Pares decrescentes de %d até 0' % num)
paresDecrescente(num)

imprime('Pares crescentes de 0 até %d' % num)
paresCrescente(num)
