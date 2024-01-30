# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20
#elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros
#vetores.
#criando 2 listas que serão usadas para formar a terceira
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = ['a', 'b', 'c',' d', 'e', 'f', 'g', 'h', 'i', 'j']
lista3 = [ ]


#repitindo em repetições do tamanho do comprimento da minha lista1:
for adicionando in range(len(lista1)):
    lista3.append(lista1[adicionando])#adicione na lista3 a lista1[um valor a cada repetição]
    lista3.append(lista2[adicionando])#adicione na lista3 a lista2[um valor a cada repetição]



    

   

print(lista3)


