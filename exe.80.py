lista = []
for c in range(0, 5):
    n  = int(input("Digite um valor: "))
    if c == 0 or n > lista[-1]:
       lista.append(n)
       print("Adicionado na última posição")
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f"Adiciona na posição {pos}")
                break
            pos += 1
            
print('-=' *30)
print(f"Lista de forma Ordenada: {lista}")


    