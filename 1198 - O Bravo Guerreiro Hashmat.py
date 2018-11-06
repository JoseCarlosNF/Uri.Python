# 1198 - Bravo Guerreiro Hashmat

while True:
  try:
    a, b = map(int,input().split())
    print(abs(a-b))
  except EOFError:
    break