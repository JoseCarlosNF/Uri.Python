def duracaoDoJogo(horaInicial, minutoInicial, horaFinal, minutoFinal):
    """ Retorna a duração do jogo em horas e minutos """

# Casos Especiais
    if horaInicial > horaFinal and minutoFinal < minutoInicial:
        horasDeDuracao = (horaFinal - horaInicial) - (-23)
        minutosDeDuracao = (minutoFinal - minutoInicial) - (-60)
        return horasDeDuracao, minutosDeDuracao
    elif horaInicial == horaFinal and minutoFinal > minutoInicial:
        horasDeDuracao = 0
        minutosDeDuracao = minutoFinal - minutoInicial
        return horasDeDuracao, minutosDeDuracao

# Casos Gerais
    # Horas
    if horaInicial == horaFinal:
        horasDeDuracao = 24
    else:
        horaInicial = horaInicial
        horaFinal = horaFinal
        horasDeDuracao = horaFinal - horaInicial

    # Minutos
    if minutoFinal < minutoInicial:
        minutosDeDuracao = 60 - abs(minutoFinal - minutoInicial)
        horasDeDuracao -= 1
    else:
        minutosDeDuracao = (minutoFinal - minutoInicial)

    # Retorno
    return horasDeDuracao, minutosDeDuracao

""" Saida Regular """

# horaInicial, minutoInicial, horaFinal, minutoFinal = map(int, input().split())

# duracaoEmHoras, duracaoEmMinutos = duracaoDoJogo(horaInicial, minutoInicial,
#                                                  horaFinal, minutoFinal)

# print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(duracaoEmHoras,
#                                                       duracaoEmMinutos))

""" Testes """

print(duracaoDoJogo(10, 12, 10, 11))  # 23, 59
print(duracaoDoJogo(7, 8, 9, 10))  # 2, 2
print(duracaoDoJogo(7, 10, 8, 9))  # 0, 59
print(duracaoDoJogo(7, 7, 7, 7))  # 24, 0
print(duracaoDoJogo(1, 1, 1, 1))  # 24, 0
print(duracaoDoJogo(1, 1, 1, 0))  # 23, 59
print(duracaoDoJogo(1, 59, 2, 59))  # 1, 0
print(duracaoDoJogo(10, 12, 12, 12))  # 2, 0
print(duracaoDoJogo(1, 1, 1, 2))  # 0, 1
print(duracaoDoJogo(10, 12, 12, 13))  # 2, 1
print(duracaoDoJogo(11, 23, 10, 22))  # 22, 59
print(duracaoDoJogo(11, 39, 19, 15))  # 7, 36
print(duracaoDoJogo(1, 59, 2, 58))  # 0, 59
print(duracaoDoJogo(7, 9, 6, 1))  # 22, 52
