# Inicialização de variáveis
total_colaboradores = 0
total_gasto_abonos = 0
total_valor_minimo = 0
maior_valor_abono = 0

# Lista para armazenar salários e abonos
salarios_abonos = []

# Flag para controle do loop
continuar = True

# Loop para entrada de dados
while continuar:
    salario = float(input("Salário (digite 0 para encerrar): "))
    
    if salario == 0:
        continuar = False  # Altera a flag para encerrar o loop
    
    # Cálculo do abono
    abono = 0.2 * salario if 0.2 * salario > 100 else 100
    
    # Atualização das variáveis
    total_colaboradores += 1
    total_gasto_abonos += abono
    total_valor_minimo += (abono == 100)  # Se o abono for 100, incrementa 1
    
    # Verifica se o abono atual é o maior
    if abono > maior_valor_abono:
        maior_valor_abono = abono
    
    # Adiciona salário e abono à lista
    salarios_abonos.append((salario, abono))

# Exibição dos resultados
print("\nProjeção de Gastos com Abono")
print("=============================")
print("Salário - Abono")
for salario, abono in salarios_abonos:
    print(f"R$ {salario:.2f} - R$ {abono:.2f}")

print(f"Foram processados {total_colaboradores} colaboradores")
print(f"Total gasto com abonos: R$ {total_gasto_abonos:.2f}")
print(f"Valor mínimo pago a {total_valor_minimo} colaboradores")
print(f"Maior valor de abono pago: R$ {maior_valor_abono:.2f}")
