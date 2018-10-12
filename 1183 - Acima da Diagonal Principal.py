# 1183 - Acima da Diagonal Principal

operacao = input().upper()
soma = 0

for l in range(12):
    for c in range(12):
        valor = float(input())
        if l < c:
            soma += valor

if operacao == 'S':
    print('%.1f' % soma)
elif operacao == 'M':
    print('%.1f' % (soma / 66.0))
