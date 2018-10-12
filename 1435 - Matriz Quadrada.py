# 1435 - Matriz Quadrada

ordem = 1
count = 1
while ordem != 0:

    # Entrada da ordem da matriz
    ordem = int(input())

    # Caso a ordem da matriz seja 0
    if ordem == 0:
        break

    # Percorrer/Imprimir a Matriz
    l=1
    while l <= ordem:
        c=1
        while c <= ordem:
            aux = l

            if c< aux:
                aux = c
            if ordem-l+1 < aux:
                aux = ordem-l+1
            if ordem-c+1 < aux:
                aux = ordem-c+1
            if count <= ordem:
                if count == 1:
                    print("%3d" % aux, end='')
                if count != 1:
                    print("%4d" % aux, end='')
                count += 1
                if count == ordem+1:
                    print()
                    count = 1
            c += 1
        l += 1
    print()
