# Inicializando um vetor com zeros para armazenar os votos de cada sistema operacional
votos = [0, 0, 0, 0, 0, 0]

# Função endemoniada para exibir os resultados
def exibir_resultados():
    print("Sistema Operacional     Votos     %")
    print("-------------------     -----     ---")
    
    total_votos = sum(votos)
    
    opcoes = ["Windows Server", "Unix", "Linux", "Netware", "Mac OS", "Outro"]
    
    sistema_mais_votado = opcoes[0]
    votos_mais_votado = votos[0]
    
    for x in range(1, len(opcoes)):
        percentual = (votos[x] / total_votos) * 100 if total_votos > 0 else 0
        print(f"{opcoes[x]:<23} {votos[x]:<9} {percentual:.2f}%")
        
        # Verifica se o sistema atual tem mais votos que o mais votado até agora
        if votos[x] > votos_mais_votado:
            sistema_mais_votado = opcoes[x]
            votos_mais_votado = votos[x]
    
    print("-------------------     -----     ---")
    print(f"Total {total_votos}")
    print(f"O Sistema Operacional mais votado foi o {sistema_mais_votado}, com {votos_mais_votado} votos, correspondendo a {((votos_mais_votado / total_votos) * 100):.2f}% dos votos.")

# Loop para receber os votos
while True: 
    voto = input("Informe o voto (1 a 6, 0 para encerrar): ")
    
    if voto == '0':
        break  # Encerra o loop se o usuário digitar 0
    elif voto.isdigit() and 1 <= int(voto) <= 6:
        votos[int(voto) - 1] += 1  # Incrementa o voto na posição correta do vetor
    else:
        print("Por favor, insira um valor válido (1 a 6).")

# Exibe os resultados
exibir_resultados()
