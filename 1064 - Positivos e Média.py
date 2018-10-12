# 1064 - Positivos e Média

'''
1. Ler 6 valores (separadamente)
2. Difernciar quantos são positivos
3. Calcular a media entre os numeros positivos com uma casa decimal
'''

leituras = 0
contador = 0
soma = 0

# Entradas / Definição
while leituras < 6:
    valor = float(input())
    if valor >= 0:
        contador += 1
        soma += valor
    leituras += 1

# Saida
print("%d valores positivos" % contador)
print("%.1f" % (soma/contador))
