# 1178 - Preenchimento de Vetor III

x = float(input())

vetor = [x]


for i in range(99):
    vetor.append(vetor[i]/2.0)

for i in range(100):
    print('N[%d] = %.4f' % (i, vetor[i]))