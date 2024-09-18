lista = []
escolha = str().upper()

while escolha != 'n':
    lista.append(int(input("Digite um valor: ")))
    escolha = str(input("Você continuar [S/N]: "))
    if escolha == 's':
        continue
    elif escolha == "n":
        break
    else:
        print(f"Ops essa opção não existe: {escolha}")
        escolha = str(input("Escolha novamente. Você continuar [S/N]: "))

print()
print(f'Foram digitados {len(lista)} números.')
print()

lista.sort(reverse=True)
print(f'Lista de forma decrescente {lista}')
print()

if 5 in lista:
    print(f'O valor 5 faz parte da lista')
else:
    print(f'O valor 5 não foi encontrado na lista')
