nome_atleta = input("Digite o nome do atleta (ou 'sair' para encerrar): ")

while nome_atleta.lower() != 'sair':
    # Inicializar lista para armazenar os saltos
    saltos = []
    
    # Coletar os cinco saltos
    for i in range(1, 6):
        salto = float(input(f"Digite a distância do {i}º salto em metros: "))
        saltos.append(salto)
    
    # Calcular a média dos saltos
    media_saltos = sum(saltos) / len(saltos)
    
    # Exibir os resultados
    print("\nResultado final:")
    print(f"Atleta: {nome_atleta}")
    print(f"Saltos: {' - '.join(map(str, saltos))}")
    print(f"Média dos saltos: {media_saltos:.2f} m\n")


# Solicitar o nome do próximo atleta ou opção para sair
nome_atleta = input("Digite o nome do próximo atleta (ou 'sair' para encerrar): ")
