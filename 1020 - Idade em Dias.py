'''

idade_dias = int(input())
anos = int(idade_dias // 365)
meses = int(idade_dias % 365 // 30)
dias = int(idade_dias % 365 % 30)

print('%d anos (s)\n' % anos)
print('%d mes (es)\n' % meses)
print('%d dia (s)\n' % dias)

'''

valor = int(input())
ano = int(valor / 365)
mes = int((valor % 365 / 30))
dia = int(valor % 365 % 30)

print('%d ano(s)\n%d mes(es)\n%d dia(s)' %(ano,mes,dia))