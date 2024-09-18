valores = list(range(0, 5))
valorNovo = []
mai = 0
men = 0

for p in valores:
    valorNovo.append(int(input(f"Informe um valor para a posição {p}: ")))
    if p == 0:
        mai = men = valorNovo[p]
    else:
        if valorNovo[p] > mai:
            mai = valorNovo[p]
        if valorNovo[p] < men:
            men = valorNovo[p]

print('=-' *30)
print(f"Os valores informado foram {valorNovo}")
print(f"O maior valor digitado na lista é {mai} na posição ", end='')
for i, v in enumerate(valorNovo):
    if v == mai:
        print(f'{i}... ', end='')
print()


print(f"O menor valor digitado na lista é {men} na posição ", end='')
for i, v in enumerate(valorNovo):
    if v == men:
        print(f'{i}... ', end='')
print()
