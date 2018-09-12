valor = input().split(" ")

a, b, c = valor
pi = 3.14159

# Area triangulo retangulo base A altura C
triangulo = (float(a) * float(c)) / 2

# Area do circulo de raio C 
circulo = pi * (float(c) * float(c))

# Area do trapezio bases AB altura C 
trapezio = float(c) * (float(a) + float(b)) / 2
# Area do quadrado de lado B
quadrado = float(b) * float(b)

# Area do retangulo AB
retangulo = float(a) * float(b)

print("TRIANGULO: %0.3f\nCIRCULO: %0.3f\nTRAPEZIO: %0.3f\nQUADRADO: %0.3f\nRETANGULO: %0.3f" % (triangulo, circulo, trapezio, quadrado, retangulo)) 