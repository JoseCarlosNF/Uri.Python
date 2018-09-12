vetor1 = input().split(" ")
vetor2 = input().split(" ")

codigo1, qtde1, valor1 = vetor1
codigo2, qtde2, valor2 = vetor2

total = (int(qtde1) * float(valor1)) + (int(qtde2) * float(valor2))

print("VALOR A PAGAR: R$ %0.2f" %total)