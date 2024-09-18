lista = []
listaPar = []
listaImpar = []

escolha = str().upper()

while escolha != 'n':
    digite = int(input("Digite um valor: "))
    lista.append(digite)

    escolha = str(input("Você continuar [S/N]: "))
    if escolha == 's':
        continue
    
    for v in lista:
        if v % 2 == 0:
            listaPar.append(v)
        else:
            listaImpar.append(v)

print(f'Lista completa é: {lista}')
print(f'Lista de Pares é: {listaPar}')
print(f'Lista de Ímpares é: {listaImpar}')
