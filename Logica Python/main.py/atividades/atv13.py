# 13 Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma
#lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da
#média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . .. ).



ano_temperatura = []

# for loop para coletar os dados
for coletar in range(12):
    mes = coletar + 1  # Corrigido para atribuir automaticamente o mês correto
    temperatura = float(input(f"Diga a temperatura (em graus Celsius) para o mês {mes}: "))

    A_T = {"Mês": mes, "Temperatura C°": temperatura}
    ano_temperatura.append(A_T)

# Calcular média anual
soma_temperaturas = sum(A_T['Temperatura C°'] for A_T in ano_temperatura)
media_anual = soma_temperaturas / len(ano_temperatura)

# Mostrar temperaturas acima da média anual
print("AS temperaturas acima da média anual:")


for A_T in ano_temperatura:
    if A_T['Temperatura C°'] > media_anual:
        mes_extenso = {
            1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril',
            5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto',
            9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'
        }
        print(f"{mes_extenso[A_T['Mês']]}: {A_T['Temperatura C°']} C°")

