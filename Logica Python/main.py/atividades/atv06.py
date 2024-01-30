
#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0. 


alunos = 10

media = [ ]





for nota in range(1, alunos+1):

    aluno1_nota1 = float(input("aluno, Digite sua nota refetente a prova 1 :"))
    aluno1_nota2 = float(input("aluno, Digite sua nota refetente a prova 2 :"))
    aluno1_nota3 = float(input("aluno, Digite sua nota refetente a prova 3 :"))
    aluno1_nota4 = float(input("aluno, Digite sua nota refetente a prova 4 :"))
      


#calculando media

total_aluno1 = aluno1_nota1 + aluno1_nota2 + aluno1_nota3 + aluno1_nota4
media= total_aluno1 / 4

#adicionando a lista
media.append(media)



#acima da media

aprovados = sum(1 for media in media if media >= 7.0)

print(aprovados)