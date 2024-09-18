espre = str(input("Digite uma expresão: "))
pilha = []

for simb in espre:
    if simb == '(':
        pilha.append('(')
    elif simb == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print("Sua expresão está válida")
else:
    print("Sua expresão está errada")