#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números
#pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.


#5)Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

#primeiro faço os vetores vazios 
listapar = [ ]
listaimpar = [ ]


# agora faço o esquema para definir os numeros que são pares e deixar guardado
def is_par(numero):
    return int(numero) % 2 == 0


# farei o loop reponsavel por adicionar os numeros impares e pares
for listatotal in range (20): #o range vai indicar quantos elementos vai ter na lista vazia
    while True: 
        lista = input(f'digite { listatotal + 1}° numero: ')
        if lista.isdigit():
            lista = int(lista)
            if is_par(lista): # se o numero da lista for par, adiciona em listapar
             listapar.append(lista)
            else:# como ja armazenei os pares, logo os que não encaixarem serão impares
                listaimpar.append(lista) 
            break #me obrigue a não usar break gabriel, tente me obrigar
        else: #nem precisava dessa merda
            print('erro tente novamente')


# eu tinha esquescido KKKKKKKKK, fiz a variavel dos numeros todos digitados
listacompleta = listaimpar + listapar          
        
print(listacompleta)
print(listaimpar)
print(listapar)