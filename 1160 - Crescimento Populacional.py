# 1160 - Crescimento Populacional


# Entradas
T = int(input())

for i in range(0, T):

    PA, PB, G1, G2 = input().split()

    PA = int(PA)
    PB = int(PB)
    G1 = float(G1)
    G2 = float(G2)

    # Logica
    anos = 0  # Reset dos anos
    while PA <= PB:
        PA += (PA * (G1 / 100)) // 1
        PB += (PB * (G2 / 100)) // 1
        anos += 1

    # Saida
    if anos <= 100:
        print("%d anos." % anos)
    else:
        print("Mais de 1 seculo.")
