'''escreva um algoritimo que calcule a tabuada de todos os numeros de 1 ate 10 , e, para cada numero vamos calcular a tabuada multplicando pelo intervalo de 1 a 10'''

''' 2 while
2 for 
while/ for'''


#calculo com for
#2 x for
for tabuada in range(1, 11, 1):
    print(f'TABUADA DO {tabuada}:')
    for i in range(1, 11, 1):
        print(f'{tabuada} x {i} = {tabuada * i}')

#com while/for
tabuada = 1
while tabuada <= 10:
    print(f'TABUADA DO {tabuada}:')
    for i in range(1, 11, 1):
        print(f'{tabuada} x {i} = {tabuada * i}')
    tabuada += 1 
