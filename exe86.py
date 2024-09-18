
# Como podemos perceber existe 1 lista contendo mais 3 lista dentro.
# [[ ], [ ], [ ]]
#   0    2    3
# Na lista (0) adicionamos 3 valores. Na lista (1) também. E na lista (2) também.
#   [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#        0          1          2
# O que fez nos chegarmos no resultado e o seguinte. Como nós chamamos esses valores:
# [1, 2, 3]
#  0  1  2
#     0
# Me mostre o número da lista 0 na posição 0 = 1.
# Me mostre o número da lista 0 na posição 1 = 2.
# Me mostre o número da lista 0 na posição 2 = 3.
# Da mesma forma se aplica aos outros. Observação é necessário ter uma variável para cada lista, o qual essa variável ira inserir o valor dentro da lista.

listaUnica = [[], [], []]
num = numD = numU =  0

for c in range(0, 3):
    num = int(input(f'Digite um valor para {0, c}: '))
    listaUnica[0].append(num)
    
for n in range(0, 3):
    numD = int(input(f'Digite um valor para {1, n}: '))
    listaUnica[1].append(numD)

for n in range(0, 3):
    numU = int(input(f'Digite um valor para {2, n}: '))
    listaUnica[2].append(numU)

print('-='*30)

print(f'[ {listaUnica[0][0]} ][ {listaUnica[0][1]} ][ {listaUnica[0][2]} ] ')
print(f'[ {listaUnica[1][0]} ][ {listaUnica[1][1]} ][ {listaUnica[1][2]} ] ')
print(f'[ {listaUnica[2][0]} ][ {listaUnica[2][1]} ][ {listaUnica[2][2]} ] ')
