# 1042 - Sort Simples

'''
1. Ler 3 valores inteiros
2. Ordenar de forma crescente +
3. Imprimir os valores em orddem crescente + uma linha em branco
4. Imprimir os valores na sequencia em que foram lidos
'''

# Entrada
a, b, c = map(int, input().split())

_1, _2,_3 = a,b,c

# Ordenamento
if a < b:
    aux = a
    a = b
    b = aux
if b < c:
    aux = b
    b = c
    c = aux
if c > b:
    aux = c
    c = b
    b = aux
if b > a:
    aux = b
    b = a
    a = aux

print("%d" % c)
print("%d" % b)
print("%d\n" % a)
print("%d" % _1)
print("%d" % _2)
print("%d" % _3)
