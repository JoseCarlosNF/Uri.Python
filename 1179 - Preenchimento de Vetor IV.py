# 1179 - Preenchimento de Vetor IV
par = []
impar = []

for i in range(15):
    # Entrada dos valores
    valor = int(input())
    if (valor % 2 == 0):
        par.append(valor)
    else:
        impar.append(valor)

    # Encher
        # Par
    if len(par) == 5:
        for n in range(5):
            print('par[%d] = %d' % (n, par[n]))
        par = []
        # Impar
    if len(impar) == 5:
        for n in range(5):
            print('impar[%d] = %d' % (n, impar[n]))
        impar = []

# Saida
    # Impar
for n in range(len(impar)):
    if impar[n] != 0:
        print('impar[%d] = %d' % (n, impar[n]))
    # Par
for n in range(len(par)):
    if par[n] != 0:
        print('par[%d] = %d' % (n, par[n]))
            