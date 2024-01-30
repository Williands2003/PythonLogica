#Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
#encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser
#armazenado). Após esta entrada de dados, faça:




# Inicialização das variáveis
notas = []
valor = 0

# Entrada de dados
while valor != -1:
    valor = float(input("Informe a nota (-1 para encerrar): "))
    if valor != -1:
        notas.append(valor)

# 1 Quantidade de valores lidos
quantidade_valores = len(notas)

# 2 Exibição dos valores na ordem em que foram informados
print(f"Valores informados: {', '.join(map(str, notas))}")

# 3 Exibição dos valores na ordem inversa
print("Valores na ordem inversa:")
for nota in reversed(notas):
    print(nota)

# 4 Soma dos valores
soma_valores = sum(notas)

# 5 Média dos valores
media_valores = soma_valores / quantidade_valores if quantidade_valores > 0 else 0

# 6 Quantidade de valores acima da média
acima_da_media = sum(1 for nota in notas if nota > media_valores)

# 7 Quantidade de valores abaixo da média
abaixo_da_media = sum(1 for nota in notas if nota < media_valores)

# Resultados
print(f"\nQuantidade de valores lidos: {quantidade_valores}")
print(f"Soma dos valores: {soma_valores}")
print(f"Média dos valores: {media_valores}")
print(f"Quantidade de valores acima da média: {acima_da_media}")
print(f"Quantidade de valores abaixo da média: {abaixo_da_media}")
