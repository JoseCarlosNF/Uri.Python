# 1118 - Varias Notas Com Validacao

codigo = 1

while codigo == 1:

    # Reset das notas em caso de outras chamadas
    nota1 = nota2 = 0

# Entrada das notas
    nota1 = float(input())
    while (nota1 < 0) or (nota1 > 10):
        print("nota invalida")
        nota1 = float(input())

    nota2 = float(input())
    while (nota2 < 0) or (nota2 > 10):
        print("nota invalida")
        nota2 = float(input())

# Media
    media = (nota1 + nota2) / 2
    print("media = %.2f" % media)

# Leitura codigo
    codigo = int(input("novo calculo (1-sim 2-nao)\n"))

# Caso codigo errado
    while (codigo != 1) and (codigo != 2):
        codigo = int(input("novo calculo (1-sim 2-nao)\n"))

# Caso os codigos certos
    if codigo == 1:
        continue
    elif codigo == 2:
        break
