# 1182 - Coluna na Matriz

Matriz = []
linha = []
soma = 0

linha = int(input())
operacao = input()

for l in range(12):
    for c in range(12):
        valor = float(input())
        if c == linha:
            soma += valor

if operacao == 'S':
    print('%.1f' % soma)
elif operacao == 'M':
    print('%.1f' % (soma/12.0))
