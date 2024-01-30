# 12 Criaando uma lista de alunos com idade e altura
biblioteca_alunos = []

# for loop para coletar os dados
for coletar in range(30):
    idade = int(input(f"Diga a idade do aluno {coletar + 1}: "))
    altura = float(input(f"Diga a altura (em metros) do aluno {coletar + 1}: "))

    aluno = {"idade": idade, "altura": altura}
    biblioteca_alunos.append(aluno)

# Inicializar a contagem de alunos abaixo da média
media_baixa_alunos = 0

# Loop para verificar alunos abaixo da média
for aluno in biblioteca_alunos:
    if aluno['idade'] > 13 and aluno['altura'] < media_altura:
        media_baixa_alunos += 1

print(f"Quantidade de alunos com mais de 13 anos e altura inferior à média: {media_baixa_alunos}")



