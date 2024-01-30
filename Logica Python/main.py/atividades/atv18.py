def calcular_percentual(votos_jogador, total_votos):
    return (votos_jogador / total_votos) * 100

num_jogadores = 23
votos = [0] * num_jogadores

# Coleta de votos
while True:
    try:#indicando que pode haver exceção , não saquei muito ele, pedi o chat gpt dicas de como fazer isso (sem me dar a respota), e me deu ele como indicação
        numero_jogador = int(input("Número do jogador (0=fim): "))
        
        if 1 <= numero_jogador <= num_jogadores:
            votos[numero_jogador - 1] += 1
        elif numero_jogador == 0:
            break
        else:
            print("Informe um valor entre 1 e 23 ou 0 para sair!")

    except ValueError:
        print("Por favor, insira um número válido.")

total_votos = sum(votos)

# Saída dos resultados
print("\nResultado da votação:")
print(f"Foram computados {total_votos} votos.")

for i, votos_jogador in enumerate(votos):
    if votos_jogador > 0:
        percentual = calcular_percentual(votos_jogador, total_votos)
        print(f"Jogador {i + 1} Votos {votos_jogador} {percentual:.1f}%")

# Encontrar o melhor jogador
melhor_jogador = votos.index(max(votos)) + 1
percentual_melhor = calcular_percentual(votos[melhor_jogador - 1], total_votos)

# Saída do melhor jogador
print(f"\nO melhor jogador foi o número {melhor_jogador}, com {votos[melhor_jogador - 1]} votos, correspondendo a {percentual_melhor:.1f}% do total de votos.")

# Gravação dos resultados em um arquivo
with open("resultado_enquete.txt", "a") as arquivo:
    arquivo.write("\nResultado da votação:\n")
    arquivo.write(f"Foram computados {total_votos} votos.\n")

    for i, votos_jogador in enumerate(votos):
        if votos_jogador > 0:
            percentual = calcular_percentual(votos_jogador, total_votos)
            arquivo.write(f"Jogador {i + 1} Votos {votos_jogador} {percentual:.1f}%\n")

    arquivo.write(f"\nO melhor jogador foi o número {melhor_jogador}, com {votos[melhor_jogador - 1]} votos, correspondendo a {percentual_melhor:.1f}% do total de votos.\n")

print("Resultados adicionados no arquivo 'resultado_enquete.txt'")
