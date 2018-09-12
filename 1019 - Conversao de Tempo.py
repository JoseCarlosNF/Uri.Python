duracao_em_segundos = int(input('duracao_em_segundos: '))
horas = duracao_em_segundos // 3600
minutos = (duracao_em_segundos % 3600) // 60
segundos = ((duracao_em_segundos % 3600) % 60)

print('%d:%d:%d' % (horas, minutos, segundos))