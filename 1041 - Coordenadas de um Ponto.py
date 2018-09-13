# 1041 -Coordenadas de um Ponto

'''
1. Ler 2 valores decimais (x,y).
2. Determinar em qual quadrante do sistema cartesiano se encontra
    2.1 Ou se está sobe um eixo
        2.1.1 Se sobe um dos eixos imprimir 'Eixo X' ou 'Eixo Y'
    2.2 Ou na origem (x= y= 0)
        2.2.1 Se na origem imprimir 'Origem'
'''

# Entrada
x, y = map(float, input().split())

# Origem
if x == y == 0:
    print('Origem')

# Sobe um eixo
elif x == 0:
    print('Eixo Y')
elif y == 0:
    print('Eixo X')

# Determinação de Quadrante
elif x > 0 and y > 0:
    print('Q1')
elif x < 0 and y > 0:
    print('Q2')
elif x < 0 and y < 0:
    print('Q3')
elif x > 0 and y < 0:
    print('Q4')
