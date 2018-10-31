# -*- coding: utf-8 -*-
# 1050 - DDD

cidades = ('Brasilia', 'Salvador', 'Sao Paulo', 'Rio de Janeiro', 'Juiz de Fora', 'Campinas', 'Vitoria', 'Belo Horizonte')

numeros = (61, 71, 11, 21, 32, 19, 27, 31)

ddd = int(input())

if ddd in numeros:
    print(cidades[numeros.index(ddd)])
else:
    print('DDD nao cadastrado')
