# 1080 - Maior e Posição

'''
1. Ler 100 inteiros
2. Apresentar o maior valor lido
'''

numeroDeLeituras = 100
leituraAtual = 1
maiorValor = 0
posicao = 0
posicaoTotal = 0

while leituraAtual < (numeroDeLeituras + 1):
    valorAtual = int(input())
    posicaoTotal += 1
    if valorAtual > maiorValor:
        maiorValor = valorAtual
        posicao = posicaoTotal
    leituraAtual += 1

print("%d" % maiorValor)
print("%d" % posicao)
