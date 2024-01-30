#11. Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

#não vou precisar mudar muita coisa, como não restringiu de usar 3 listas, vou apenas criar mais uma lista e adicionar +1 linha no for loop

#criando 3 listas que serão usadas para formar a quarta
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = ['=', '=', '=',' =', '=', '=', '=', '=', '=', '=']
lista3 = ['a', 'b', 'c',' d', 'e', 'f', 'g', 'h', 'i', 'j']
lista_intercalada = []



#repitindo em repetições do tamanho do comprimento da minha lista1:
for adicionando in range(len(lista1)):
    lista_intercalada.append(lista1[adicionando])#adicione na lista_intercalada um valor da lista1[um valor a cada repetição]
    lista_intercalada.append(lista2[adicionando])#adicione na lista_intercalada um valor da lista2[um valor a cada repetição]
    lista_intercalada.append(lista3[adicionando])#adicione na lista_intercalada um valor da lista3[um valor a cada repetição]





   

print(lista_intercalada)