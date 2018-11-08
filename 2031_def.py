# -*- coding: utf-8 -*-
# 2031 - Pedra, Pepal, Ataque Aereo


# Função (retorna o ganhador do round)
def ganhador(entrada1, entrada2):

    # Ataque vs. Pedra
    if entrada1 == 'ataque' and entrada2 == 'pedra':
        ganhador = 'Jogador 1 venceu'
    elif entrada1 == 'pedra' and entrada2 == 'ataque':
        ganhador = 'Jogador 2 venceu'

    # Pedra vs. Papel
    elif entrada1 == 'pedra' and entrada2 == 'papel':
        ganhador = 'Jogador 1 venceu'
    elif entrada1 == 'papel' and entrada2 == 'pedra':
        ganhador = 'Jogador 2 venceu'

    # Papel vs. Ataque
    elif entrada1 == 'papel' and entrada2 == 'ataque':
        ganhador = 'Jogador 2 venceu'
    elif entrada1 == 'ataque' and entrada2 == 'papel':
        ganhador = 'Jogador 1 venceu'

    # Papel vs. Papel
    elif entrada1 == 'papel' and entrada2 == 'papel':
        ganhador = 'Ambos venceram'

    # Pedra vs. Pedra
    elif entrada1 == 'pedra' and entrada2 == 'pedra':
        ganhador = 'Sem ganhador'

    # Ataque vs. Ataque
    elif entrada1 == 'ataque' and entrada2 == 'ataque':
        ganhador = 'Aniquilacao mutua'

    return ganhador


# Main
n = int(input())
for i in range(n):
    entrada1 = input()
    entrada2 = input()
    print(ganhador(entrada1, entrada2))