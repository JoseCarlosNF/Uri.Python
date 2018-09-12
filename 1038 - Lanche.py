# 1038 - Lanche

'''
1. ler codigo do produto
2. Ler quantidade do produto
3. Imprimir valor a ser pago
'''

lista = input().split(' ')
codigo, quantidade = lista
codigo = int(codigo)
quantidade = int(quantidade)

if codigo == 1:
    pagar = quantidade * 4.00
elif codigo == 2:
    pagar = quantidade * 4.50
elif codigo == 3:
    pagar = quantidade * 5.00
elif codigo == 4:
    pagar = quantidade * 2.00
elif codigo == 5:
    pagar = quantidade * 1.50
else:
    print('Codigo invalido')

print('Total: R$ %.2f' % pagar)
