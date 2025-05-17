'''escreva um algoritimo que calcule a tabuada de todos os numeros de 1 ate 10 , e, para cada numero vamos calcular a tabuada multplicando pelo intervalo de 1 a 10'''

''' 2 while
2 for 
while/ for'''

# 2 x while
tabuada = 1
while tabuada <= 10:
   print(f'TABUADA DO {tabuada}:')
   i = 1
   while i <= 10:
     print(f'{tabuada} x {i} = {tabuada * i}')
     i += 1
   tabuada += 1
