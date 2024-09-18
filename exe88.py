import random
import time

print('-'*57)
print('                       MEGA SENA                     ')
print('-'*57)
lista = list()

jogada = int(input('Quantos jogos você quer que eu sorteie? '))
print('-='*3, f'SORTEANDO {jogada} JOGOS', '-='*3)

for j in range(jogada):
    time.sleep(1)
    if lista == lista:
        n = list(random.sample(range(1, 60), 6))
        lista.clear()
        lista.append(n)            
        print(f'{j+1} - {lista}')
