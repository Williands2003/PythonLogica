#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação 
#no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

pessoa1 = {
 "altura" : "",
 "idade" : ""
   
}
pessoa2 = {
 "altura" : "",
 "idade" : ""
   
}
pessoa3 = {
 "altura" : "",
 "idade" : ""
   
}
pessoa4 = {
 "altura" : "",
 "idade" : ""
   
}
pessoa5 = {
 "altura" : "",
 "idade" : ""
   
}


# Loop para obter informações de cada pessoa
for x, pessoa in enumerate([pessoa1, pessoa2, pessoa3, pessoa4, pessoa5], 1):
    altura = float(float(input(f"Digite a altura da pessoa {x}: ")))
    idade = int(input(f"Digite a idade da pessoa {x}: "))

    # Atribuindo valores aos dicionários
    pessoa["altura"] = altura
    pessoa["idade"] = idade

# Imprimindo as informações de cada pessoa
for i, pessoa in enumerate([pessoa1, pessoa2, pessoa3, pessoa4, pessoa5], 1):
    print(f"Pessoa {i}: Altura = {pessoa['altura']}, Idade = {pessoa['idade']}")

