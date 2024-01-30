# Carregando a lista de modelos de carros
modelos = ["Fusca", "Gol", "Uno", "Vectra", "Peugeot"]

# Carregando a lista de consumo em km/l para cada carro
consumo = [7, 10, 12.5, 9, 14.5]

# Calculando o modelo mais econômico
indice_mais_economico = consumo.index(min(consumo))

# Inicializando variáveis para o relatório final
relatorio_final = []

# Calculando e gerando o relatório final
for i in range(len(modelos)):
    # Calculando litros necessários para percorrer 1000 km
    litros_necessarios = 1000 / consumo[i]
    
    # Calculando o custo considerando o preço da gasolina
    custo = litros_necessarios * 2.25
    
    # Adicionando informações ao relatório
    relatorio_final.append(f"{i + 1} - {modelos[i]} - {consumo[i]} - {litros_necessarios:.1f} litros - R$ {custo:.2f}")

# Exibindo o relatório final
print("Comparativo de Consumo de Combustível")
for i in range(len(modelos)):
    print(f"Veículo {i + 1}\nNome: {modelos[i]}\nKm por litro: {consumo[i]}\n")

print("Relatório Final")
for item in relatorio_final:
    print(item)

# Exibindo o modelo mais econômico
print(f"\nO menor consumo é do {modelos[indice_mais_economico]}.")
