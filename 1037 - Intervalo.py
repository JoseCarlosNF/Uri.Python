# 1037 - Intervalo

'''
Verificar em qual intervalo o valor de entrada se encontra
'''

entrada = float(input())

if 0 <= entrada <= 25.0000:
    print('Intervalo [0,25]')
elif 25.0000 < entrada <= 50.0000:
    print('Intervalo (25,50]')
elif 50.0000 < entrada <= 75.0000:
    print('Intervalo (50,75]')
elif 75.0000 < entrada <= 100.0000:
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')
