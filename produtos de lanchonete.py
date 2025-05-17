# escreva um algoritimo  que mostra, na tela quatro produtos a serem comprados em uma lanchonete:

# - cochinha - 5,00
# - pastel - 7,00
# - café - 4,00
# - suco - 6,00

print("LANCHONETE")
print("1 - coxinha $ 5,00")
print("2 - coxinha $ 7,00")
print("3 - coxinha $ 4,00")
print("4 - coxinha $ 6,00")
print("5 - sair")

total = 0
while True:
    op = int(input("qual item gostaria de comprar? "))
    
    if (op == 1):
        qtd = int(input("quantas unidades quer comprar? "))
        total = total + qtd * 5.00
    elif (op ==2):
        qtd = int(input("quantas unidades quer comprar? "))
        total = total + qtd * 7.00
    elif (op == 3):
        qtd = int(input("quantas unidades quer comprar? "))
        total = total + qtd * 4.00
    elif (op == 4):
        qtd = int(input("quantas unidades quer comprar? "))
        total = total + qtd * 6.00
    elif (op == 5):
        break
    else:

        print("produto invalido. selecione outro. ")   

print(f"\no total a ser gasto neste pedido é de $ {total}.  ") 
