
lista = [
    "Hortela", "Melancia", "Manga", "Limão", "Laranja"
]

jogos = [
    "CS:GO", "GTA V", "Valorant", "LOL", "Arma 2"
]

if __name__ == "__main__":
    
    for item in lista[0:4]:
        print(item)


    print("=" *30)

    for jogo in jogos:
        if jogo == "Valorant":
            print("Não roda, passa passa para o proximo.")
            continue
        print(jogo)
    else:
        print("Teste Executado com sucesso")