nome = str(input('Nome: '))
salario_fixo = float(input('salarioFixo: '))
total_de_vendas = float(input('totalVendas: '))

salario = salario_fixo + (0.15 * total_de_vendas)

print('TOTAL = R$ %.2f' % salario)