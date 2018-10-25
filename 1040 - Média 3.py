# 1040 - Média 3

'''
1. ler 4 notas de alunos
2. implementar peso 2, 3, 4, 1 respectivamente
3. Calcular a media entre as notas
4. Mostrar a mensagem 'Media: '
5. Se a media >= 7.0 imprimir 'Aluno aprovado'
6. Se a media < 5.0 imprimir 'Aluno reprovado'
7. Se a 5.0 <= media <= 6.9 imprimir 'Aluno em exame'
    7.1 Se em exame ler nota obtida pelo aluno no exame
    7.2 'Nota do exame: '
    7.3 Somar a nota do exame com a media anterior e dividir por 2
    7.4 Se media >= 5.0 'Aluno aprovado'
    7.5 Se media <= 4.9 'Aluno aprovado'
    7.6 Apresentar 'Media final: '
obs: todas as apresentações de nota devem ter uma casa decimal
'''

# Entrada 📩
nota1, nota2, nota3, nota4 = map(float, input().split())

# Peso das notas 📌
nota1 *= 2
nota2 *= 3
nota3 *= 4
nota4 *= 1

# Media Comum 💹
media = (nota1 + nota2 + nota3 + nota4) / 10
print('Media: %.1f' % media)

# Avaliação de Media 👁‍🗨
if media >= 7.0:
    print('Aluno aprovado.')
elif media < 5.0:
    print('Aluno reprovado.')
elif 5.0 <= media <= 6.9:
    print('Aluno em exame.')

    # Exame 👀
    notaExame = float(input())
    print('Nota do exame: %.1f' % notaExame)
    mediaFinal = (notaExame + media) / 2
    if mediaFinal >= 5.0:
        print('Aluno aprovado.')
    elif mediaFinal <= 4.9:
        print('Aluno reprovado.')

    # Apresentar Media final 🗣
    print('Media final: %.1f' % mediaFinal)
