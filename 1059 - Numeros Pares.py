# 1059 - Numeros Pares

'''
Mostrar todos os numeros pares no intervalo de 1 a 100
'''

counter = 1
while counter < 101:
    if counter % 2 == 0:
        print(counter)
    counter += 1
