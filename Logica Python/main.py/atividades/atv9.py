#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos
#quadrados dos elementos do vetor.
#lista dos numeros normais
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_C = [] #onde vai ficar a lista ao cubo
#calcular ao cubo
#para number em lista:
for number in lista:#number = variavel criada
    calculo = number ** 2 #fazemos a formula do calculo, o number vai ser um
    #numero de cada vez da lista 
    lista_C.append(calculo) #adicionando o calculo ( cada numero ao quadrado) a lista_C (lista ao cubo)
    


print(lista_C)



