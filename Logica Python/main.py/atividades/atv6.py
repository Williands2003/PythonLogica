#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média
# de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

def linha():
    return f'========================'


#criando uma função para linha (puro capricho)
alunos = 10
medias = []
no_media = []

for i in range(1, alunos+1):
    nota1 = float(input(f"Digite a nota  de ciencias do aluno {i}: "))
    nota2 = float(input(f"Digite a nota de matematica do aluno {i}: "))
    nota3 = float(input(f"Digite a nota de portugues do aluno {i}: "))
    nota4 = float(input(f"Digite a nota de ingles do aluno {i}: "))

    # Calculando a média do aluno
    media_aluno = (nota1 + nota2 + nota3 + nota4) / 4

    # Adicionando a média à lista de médias
    medias.append(media_aluno)
else:
    no_media.append(media_aluno)

# Contando o número de alunos com média maior ou igual a 7.0
aprovados = sum(1 for media in medias if media >= 7.0)

# Imprimindo o resultado

print(f"as notas na media são:{medias} ")
print(linha())
print(f"as notas baixo da media {no_media}")





