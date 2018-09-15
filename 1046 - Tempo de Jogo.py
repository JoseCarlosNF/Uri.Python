# 1046 - Tempo de Jogo

'''
1. Ler hora de inicio e termino do jogo, respectivamente
2. Calcular a duração do jogo
'''
# Entrada
horaInicio, horaTermino = map(int, input().split())

# Calculo da duração
duração = horaTermino - horaInicio

if duração < 0:
	duração = 24 + (horaTermino - horaInicio)

# Saida para 24 horas de jogo
if horaInicio == horaTermino:
	print("O JOGO DUROU 24 HORA(S)")

# Saida para outras ocasiões
else:
	print("O JOGO DUROU %d HORA(S)" % duração)
