from random import randint

if __name__ == "__main__":
    

    lista_randomicos = [randint (1, 50) for _ in range(50)]
    lista_num = []

    for num in lista_randomicos:
        if num not in lista_num:
            lista_num.append(num) 

    print(lista_randomicos)
    print(list(set(lista_randomicos)))
