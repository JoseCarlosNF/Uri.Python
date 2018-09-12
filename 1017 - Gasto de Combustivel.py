temp_viagem = int(input('temp_viagem: '))
velocidade_media = float(input('velocidade_media: '))
distancia = velocidade_media * temp_viagem

cosumo = distancia / 12

print('%.3f' % cosumo)