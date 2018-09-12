# 1021 - Cedulas e Moedas

'''
Ler um valor e distribui-lo em cedulas e moedas
da forma mais eficiente possivel
'''

N = float(input())

if (0 <= N <= 1000000.00):

    print("NOTAS:")
    notas = N / 100
    print("%d nota(s) de R$ 100.00" % notas)
    N = N % 100

    notas = N / 50
    print("%d nota(s) de R$ 50.00" % notas)
    N = N % 50

    notas = N / 20
    print("%d nota(s) de R$ 20.00" % notas)
    N = N % 20

    notas = N / 10
    print("%d nota(s) de R$ 10.00" % notas)
    N = N % 10

    notas = N / 5
    print("%d nota(s) de R$ 5.00" % notas)
    N = N % 5

    notas = N / 2
    print("%d nota(s) de R$ 2.00" % notas)
    N = N % 2

    print("MOEDAS:")
    moedas = N / 1.00
    print("%d moeda(s) de R$ 1.00" % moedas)
    N = N % 1.00

    moedas = N / 0.50
    print("%d moeda(s) de R$ 0.50" % moedas)
    N = N % 0.50

    moedas = N / 0.25
    print("%d moeda(s) de R$ 0.25" % moedas)
    N = N % 0.25

    moedas = N / 0.10
    print("%d moeda(s) de R$ 0.10" % moedas)
    N = N % 0.1

    moedas = N / 0.05
    print("%d moeda(s) de R$ 0.05" % moedas)
    N = N % 0.05

    moedas = float(N / 0.01)
    print("%0.0f moeda(s) de R$ 0.01" % moedas)
