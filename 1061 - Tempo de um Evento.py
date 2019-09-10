# Entradas
diaInicio = input().split("Dia")
horaInicio = input().split(":")
diaFim = input().split("Dia")
horaFim = input().split(":")

# >=> Logica
segundosTotais = (60 - int(horaInicio[2]) + int(horaFim[2]))
minutosTotaisEmSegundos = (60 - int(horaInicio[1]) - 1 + int(horaFim[1])) * 60
horasTotaisEmSegundos = (24 - int(horaInicio[0]) - 1 + int(horaFim[0])) * 3600
diasTotaisEmSegundos = (int(diaFim[1]) - int(diaInicio[1]) - 1) * 86400

tempoTotalEmSegundos            \
    = segundosTotais            \
    + minutosTotaisEmSegundos   \
    + horasTotaisEmSegundos     \
    + diasTotaisEmSegundos

duracaoDias = tempoTotalEmSegundos / 86400
duracaoHoras = (tempoTotalEmSegundos % 86400) / 3600
duracaoMinutos = ((tempoTotalEmSegundos % 86400) % 3600) / 60
duracaoSegundos = ((tempoTotalEmSegundos % 86400) % 3600) % 60

# Apresentação Final
print("{:d} dia(s)".format(int(duracaoDias)))
print("{:d} hora(s)".format(int(duracaoHoras)))
print("{:d} minuto(s)".format(int(duracaoMinutos)))
print("{:d} segundo(s)".format(int(duracaoSegundos)))
