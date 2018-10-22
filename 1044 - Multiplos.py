# 1044 - Multpilos

a, b = map(int, input().split())

a = abs(a)
b = abs(b)

x = 0

if ((a == b) or ((a == 0) or (b == 0))):
    print('Sao Multiplos')

elif a > b:
    while x <= a:
        y = b * x
        if y == a:
            print('Sao Multiplos')
            break
        if y > a:
            print('Nao sao Multiplos')
            break
        x += 1

elif b > a:
    while x <= b:
        y = a * x
        if y == b:
            print('Sao Multiplos')
            break
        if y > b:
            print('Nao sao Multiplos')
            break
        x += 1
