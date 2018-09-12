Linha_1 = input().split(" ")
Linha_2 = input().split(" ")
Linha_3 = input().split(" ")
Linha_4 = input().split(" ")

# Linha 1
N1, char_1_1, D1, char_meio_1, N1_2, char_2_1, D1_2 = Linha_1
N1 = int(N1)
D1 = int(D1)
N1_2 = int(N1_2)
D1_2 = int(D1_2)

# Linha 2
N2, char_1_2, D2, char_meio_2, N2_2, char_2_2, D2_2 = Linha_2
N2 = int(N2)
D2 = int(D2)
N2_2 = int(N2_2)
D2_2 = int(D2_2)

# Linha 3
N3, char_1_3, D3, char_meio_3, N3_2, char_2_3, D3_2 = Linha_3
N3 = int(N3)
D3 = int(D3)
N3_2 = int(N3_2)
D3_2 = int(D3_2)

# Linha 4
N4, char_1_4, D4, char_meio_4, N4_2, char_2_4, D4_2 = Linha_4
N4 = int(N4)
D4 = int(D4)
N4_2 = int(N4_2)
D4_2 = int(D4_2)

if char_meio == "+":
    Soma = (N1 * D1 + N1_2 * D1) / (D1 * D1_2)

if char_meio == "-":
    Subtracao = (N1 * D1_2 - N1_2 * D1) / (D1 * D1_2)

if char_meio == "*":
    Multiplicacao = (N1 * N1_2) / (D1 * D1_2)

if char_meio == "/":
    Divisao = (N1 * D1_2) / (N1_2 * D1)

print("Fim")