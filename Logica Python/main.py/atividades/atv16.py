# Inicialização das variáveis
salarios = [0] * 9  # Lista para armazenar a contagem de vendedores em cada faixa salarial

# Função para calcular o salário com base nas vendas brutas
def calcular_salario(vendas_brutas):
    salario_base = 200
    comissao_percentual = 0.09
    return salario_base + (comissao_percentual * vendas_brutas)

# Entrada de dados
num_vendedores = int(input("Digite o número de vendedores: "))

# Processamento dos salários e contagem nas faixas
for _ in range(num_vendedores):
    vendas_brutas = float(input("Digite as vendas brutas do vendedor: "))
    salario = calcular_salario(vendas_brutas)

    # Atualização da contagem nas faixas salariais
    if 200 <= salario <= 299:
        salarios[0] += 1
    elif 300 <= salario <= 399:
        salarios[1] += 1
    elif 400 <= salario <= 499:
        salarios[2] += 1
    elif 500 <= salario <= 599:
        salarios[3] += 1
    elif 600 <= salario <= 699:
        salarios[4] += 1
    elif 700 <= salario <= 799:
        salarios[5] += 1
    elif 800 <= salario <= 899:
        salarios[6] += 1
    elif 900 <= salario <= 999:
        salarios[7] += 1
    else:
        salarios[8] += 1

# Exibição dos resultados
for i in range(len(salarios)):
    inicio_faixa = 200 + i * 100
    fim_faixa = inicio_faixa + 99 if i < 8 else "em diante"
    print(f"Vendedores com salário entre ${inicio_faixa} e ${fim_faixa}: {salarios[i]}")
