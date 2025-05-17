

 # EXERCICIO 3

 #UM CINEMA COBRA PREÇOS DIFERENTES PARA OS INGRESSOS, DE ACORDO COM A IDADE DA PESSOA. SE A PESSOA TIVER MENOS DE 3 ANOS DE IDADE, O INGRESSO SERÁ GRATUITO, SE TIVER ENTRE 3 E 12 ANOS, O INGRESSO CUSTARÁ 15 REAIS, SE TIVER MAIS DE 12 ANOS, CUSTARA 39 REAIS.
 # ESCREVA UM LAÇO ONDE VOÇE PERGUNTA A IDADE  AOS USUARIOS E, ENTÃO, INFORME-LHES O PREÇO DO INGRESSO DO CINEMA..
 # ENCERRE O LAÇO, USANDO UM BREAK QUANDO O USUARIO DIGITAR ZERO.
 # APÓS ENCERRAR O LAÇO, APRESENTE NA TELA O TOTAL DE PESSOAS QUE COMPRARAM INGRESSOS, O  TOTAL DE DINHEIRO ARRECADADO E A MÉDIA DE IDADE DAS PESSOAS.

total = 0
dinheiro = 0
acc_idades = 0

while True:
    idade = int(input("qual sua idade?"))
    if idade == 0:
        break

    total += 1
    acc_idades += idade
    if idade < 3:
        ingresso = 0
    else:  
        if idade > 12 :
            ingresso = 30
        else:
            ingresso = 15

    dinheiro += ingresso

if total > 0:
     
     média = acc_idades / total
     print(f"total de pessoas: {total}")
     print(f"total arrecadao: {dinheiro}")
     print(f"média de idade: {média}")