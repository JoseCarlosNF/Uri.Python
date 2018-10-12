# 1060 - Numeros Positivos

'''
1. Ler 6 valores (separadamente)
2. Difernciar quantos são positivos
'''

leituras = 0
contador = 0

# Entradas / Definição
while leituras < 6:
    valor = float(input())
    if valor >= 0:
        contador += 1
    leituras += 1

# Saida
print("%d valores positivos" % contador)
