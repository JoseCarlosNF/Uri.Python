# 1185 - Acima da Diagonal Secundaria

operacao = input().upper()
soma = 0

for l in range(12):
    for c in range(12):
        valor = float(input())
        if 0 <= (l + c) <= 10:
            soma += valor

if operacao == 'S':
    print('%.1f' % soma)
elif operacao == 'M':
    print('%.1f' % (soma / 66.0))
