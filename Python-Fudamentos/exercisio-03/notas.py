if __name__ == "__main__":
    nt1 = float(input("Informe a primeira nota: "))
    nt2 = float(input("Informe a Segunda nota: "))
    nt3 = float(input("Informe a Terceira nota: "))
    nt4 = float(input("Informe a Quarta nota: "))
    nt5 = float(input("Informe a Quinta nota: "))
    
    lista_notas = [
        nt1 + nt2 + nt3 + nt4 + nt5
    ]

    # slice -> Fatiamento de lista
    # nova_lista = lista_notas[2:5]

    #Ordena a lista do menor para o maior quando e número e quando e string retorna em ordem afalbetica.

    lista_nova = lista_notas[1:4]

    media = sum(lista_nova) / len(lista_nova)

    print(f"A media é: {media:.2f}.")
    


    
   