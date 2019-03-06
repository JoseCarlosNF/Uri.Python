# 1049 - Animal

ave = {'carnivoro': 'aguia', 'onivoro': 'pomba'}
mamifero = {'onivoro': 'homem', 'herbivoro': 'vaca'}
vertebrado = {'ave': ave, 'mamifero': mamifero}

inseto = {'hematofago': 'pulga', 'herbivoro': 'lagarta'}
anelideo = {'hematofago': 'sanguessuga', 'onivoro': 'minhoca'}
invertebrado = {'inseto': inseto, 'anelideo': anelideo}

baseDeDados = {'vertebrado': vertebrado, 'invertebrado': invertebrado}

palavra1 = input()
palavra2 = input()
palavra3 = input()
print(baseDeDados[palavra1][palavra2][palavra3])
