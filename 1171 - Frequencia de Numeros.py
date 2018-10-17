# 1171 - Frequencia de Numeros


# Entrada (Qantidade de Numeros)
qte = int(input())

# Dicionario
dic = {}

# Entarada/Individual dos numeros
for i in range(qte):

    v = int(input())

    # Se o numero estiver no dicionario incrementar um ao valor da sua chave
    if v in dic:
        dic[v] += 1

    # Se não estiver estabelecer o valor de sua chave como um
    else:
        dic[v] = 1

# Obter o valor das chave
chaves = dic.keys()

# Ordenar o valor das chaves
chaves = sorted(chaves)

# Saida
for j in chaves:
    print("%d aparece %d vez(es)" % (j, dic[j]))
