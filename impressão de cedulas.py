# Exercicio 2 

# ESCREVA UM ALGORITIMO QUE LEIA UM VALOR E QUE IMPRIMA A QUANTIDADE DE CEDULAS NECESSARIAS PARA PAGAR ESSE MESMO VALOR. PARA SIMPLIFICAR , VAMOS TRABALHAR APENAS COM VALORES INTEIROS E COM CÉDULAS DE R$ 100, R$ 50, R$ 20, R$ 10, R$ 5, E R$1, 

valor = int(input("Digite o valor em R$: "))

while True:
    if valor >= 100:
        cont100 = valor // 100
        valor = valor - cont100 * 100
        print(f"Cédulas de 100: {cont100}")
        if not valor:
            break


    if valor >= 50:
        cont50 = valor // 50
        valor = valor - cont50 * 50
        print(f"Cédulas de 50: {cont50}") 
        if not valor:
            break   


    if valor >= 20:
        cont20 = valor // 20
        valor = valor - cont20 * 20
        print(f"Cédulas de 20: {cont20}")  
        if not valor:
            break             


    if valor >= 10:
        cont10 = valor // 10
        valor = valor - cont10 * 10
        print(f"Cédulas de 10: {cont10}")
        if not valor:
            break        


    if valor >= 5:
        cont5 = valor // 5
        valor = valor - cont5 * 5
        print(f"Cédulas de 5: {cont5}")
        if not valor:
            break


    if valor >= 1:
        cont1 = valor // 1
        valor = valor - cont1 * 1
        print(f"Cédulas de 1: {cont1}") 
        if not valor:
            break