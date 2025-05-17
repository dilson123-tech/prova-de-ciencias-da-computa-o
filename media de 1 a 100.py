#fazendo média de 1 a 100
soma = 0 #variavel pra soma
qtd = 0 # variavel contadora
for i in range(1, 101, 1):
    if (i % 2 == 0): #se for par vai somando
        soma += i
        qtd += 1
media = soma /qtd
print(f'a media dos pares de 1 até 100 é: {media}')       