
dados = list()

dados.append('Pedro')
dados.append(25)

pessoa = list()
pessoa.append(dados[:])

dados[0] = 'Lucas'
dados[1] = 30
# Abaixo estamos criando um lista pessoas para guardar os dados da lis 'dados' ou seja com essa parametro '[:]' fizemos uma copia da lista 'dados'.
pessoa.append(dados[:])
dados[0] = 'Maria'
dados[1] = 20
pessoa.append(dados[:])
#print(pessoa)

# Abaixo você ira ver como indentificamos as listas atraves de seu indice.
#pessoa = [['Pedro', 25], ['Lucas', 30], ['Maria', 20]]
#              0     1        0      1       0      1
#           |     0    |  |      1    |  |     2    |  

print(pessoa[0][0]) #-> Pedro
print(pessoa[2][0]) # -> Maria
print(pessoa[1]) # -> ['Lucas', 30]
print(pessoa[1][1]) # -> 30

for p in pessoa:
    while len(pessoa) < 0:
        len(pessoa) + p
    print(p)
'''
galera = list()
dado = list()
totalmax = totalmin = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade {p[1]}.')
        totalmax += 1
    else:
        print(f'{p[0]} é menor de idade {p[1]}.')
        totalmin += 1

print(f'Possui {totalmax} maior de idade é {totalmin} menor de idade.')

''' 
