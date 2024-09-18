listaUnica = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Informe o {c} número: '))
    if valor % 2 == 0:
        listaUnica[0].append(valor)
    else:
        listaUnica[1].append(valor)

listaUnica[0].sort()
listaUnica[1].sort()

print(f'Os números pares: {listaUnica[0]}')
print(f'os números impares: {listaUnica[1]}')
