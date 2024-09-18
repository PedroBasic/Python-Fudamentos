# As Listas[] podem ser modificadas diferente das tuplas ou seja são Mutaveis
lista = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']
print(lista)

# Utilizando listas podemos alterar os valores incluido na variavel. A alteração e realizada de acordo com o seu indice segue exemplo abaixo.
lista[3] = 'Pícole'
print(lista)

 # Caso deseja adicionar um novo elemento dentro da lista, sem precisar alterar o valor já incluso. Utilizamo o termo  append([nome_produto])
lista.append('Chocolate')
print(lista)

''' 
Caso deseja adicionar um elemento em uma posição especifica, exemplo antes do elemento suco armazenado na vatiavel lista[] utilizamos o metodo insert(indice, nome_produto).
Observalção: O elemento sempre será inserido entre indice determinado. Exemplo: temos uma lista com 5 elementos.

Se quisermos inserirmos um valor depois do elemento 0. Iremos utilizar o seguinte  metodo.

Ex:
lista: ['0', '1', '2', '3', '4']
lista.insert(1, 'Cookie')
print(lista)

Vejamos abaixo o valor foi inserido entre o indice 0 e 1.

Retorno:
lista = ['Hamburguer', 'cookie', 'Suco', 'Pizza', 'Pícole', 'Chocolate']
              0            1        2       3        4           5
'''
lista.insert(1, 'cookie')
print(lista)

# Caso desejamos excluir um elemento da lista[], temos dois metodos. del nome_variavel[indice_elemento] e nome_variavel.pop(indice_elemento).
del lista[5]
print(lista)

# Segundo exemplo pop(), e utilizado para eliminar sempre o ultimo elemento.
lista.pop(3)
print(lista)
 
# Se deseja excluir um item pelo nome do elemento inluso na lista. Utilizamos o termo remove('nome_elemento')
lista.remove('cookie')
print(lista)

# O termo IN e utilizado ara indentificar se o valor 3 IN     = " Está incluido" na lista[]

if 'Chocolate' in lista:
    lista.remove('Chocolate')
else:
    print("Não possui o valor CHOCOLATE na lista.")

lista.insert(1, 'Cookie')
print(lista)

# Termo Sort(), permite ordenar os valores dentro de uma variavel.
valores1 = [8, 9, 6, 7, 4, 5]
valores1.sort()
print(valores1)

# Podemos criar uma variavel que cria uma lista de forma automatica utilizando o termo lis(range(valores))
valores = list(range(4, 11))
print(valores)

# Abaixo criamos um programa que permite alterarmos os valores incluido na variavel, valores = list(range(4, 11)). Utilizando o metodo for solicitamos que seja digitado um novo valor para cada elemento.
listaAlter = []

for v in valores:
    print(v)
    listaAlter.append(int(input("Digite um novo valor: ")))
    listaAlter.sort()

print(f"\n Segue abaixo valores da variavel em ordem.")    
print(listaAlter)

# Caso deseja ordenar os valores de uma lista na ordem reversa. Basta utilizarmos o termo. lista.sort(reverse=true)
print(f"\n Segue Abaixo os valores em ordem reversa.")
listaAlter.sort(reverse=True)
print(listaAlter)

# Para criar uma list e permite que essa lista seja copiada os memso elementos para outra varivael, utilizamos o seguinte metodo b = a[:]. No exemplo abaixo verificamos que o valor não foi alterado para ambas as varivel,
# Porque Copiamos ela.
a = [3, 2, 5, 6]
b = a[:]
b[0] = 1
print(f'A lista A: {a}')
print(f'A lista B: {b}')