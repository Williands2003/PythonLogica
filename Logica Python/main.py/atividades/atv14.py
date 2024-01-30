#Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As
#perguntas são:
#a. "Telefonou para a vítima?"
#b. "Esteve no local do crime?"
#c. "Mora perto da vítima?"
#d. "Devia para a vítima?"
#e. "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a
#participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve
#ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso
#contrário, ele será classificado como "Inocente".
#-----------------------------------------------------------------

#função 
def pergunta1(pergunta_a):
    if pergunta_a == "S":
        return 2
    elif pergunta_a == "N":
        return 1
    else:
        print("erro,certifique de digitar S ou N")
    
        return 0 
#B
def pergunta2(pergunta_b):
    if pergunta_b == "S":
        return 2
    elif pergunta_b == "N":
        return 1
    else:
        print("erro,certifique de digitar S ou N")
    
        return 0

#c
def pergunta3(pergunta_C):
    if pergunta_c == "S":
        return 2
    elif pergunta_c == "N":
        return 1
    else:
        print("erro,certifique de digitar S ou N")
    
        return 0

#d
def pergunta4(pergunta_d):
    if pergunta_d == "S":
        return 2
    elif pergunta_d == "N":
        return 1
    else:
        print("erro,certifique de digitar S ou N")
    
        return 0

#e
def pergunta5(pergunta_e):
    if pergunta_e == "S":
        return 2
    elif pergunta_e == "N":
        return 1
    else:
        print("erro,certifique de digitar S ou N")
    
        return 0


#-----------------------------------------------------------------
#listas de ranking
inocente = ["inocente"] # 1
suspeita = ["suspeito..."] # 2
cumplice = ["Cumplice!"] #3/4 
assasino = ["Assasino! Você está preso!"] # 5
point = []
#-------------------------------------------------------------------
#input de perguntas
player = input("digite seu nome:")

pergunta_a = input("Telefonou para a vítima? (S/N):")
pergunta_b = input("Esteve no local do crime? (S/N: ")
pergunta_c = input("Mora perto da vítima? (S/N): ")
pergunta_d = input("Devia para a vítima? (S/N): ")
pergunta_e =input("Já trabalhou com a vítima? (S/N): ")
#-------------------------------------------------------------------
#esquema de pontuação

pointA = pergunta1(pergunta_a)
pointB = pergunta2(pergunta_b)
pointC = pergunta3(pergunta_c)
pointD = pergunta4(pergunta_d)
pointE = pergunta5(pergunta_e)


#___calculo
point_calculator = pointA + pointB + pointC + pointD + pointE

#___for loop para adicionar ao rank 


if point_calculator == 1:
 md5 = inocente
elif point_calculator == 2 :
  md5 = suspeita
elif point_calculator == 3 or 4:
    md5 = cumplice
elif point_calculator == 5:
  md5 = cumplice


print(f"sua pontuação foi de {point_calculator}, e abaixo veremos sua classificação: ")
print(f"jogador: {player}, seu veredito é: {md5}")







