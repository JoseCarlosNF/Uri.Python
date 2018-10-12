# 1181 - Linha Matriz

linha = int(input())  # linha
operacao = input().upper()  # operacao
soma = 0

for l in range(12):  # linha
    for c in range(12):  # coluna
        valor = float(input())
        if l == linha:
            soma += valor

if operacao == 'S':
    print('%.1f' % soma)
elif operacao == 'M':
    print('%.1f' % (soma / 12.0))
