"""
 O laço while e utilizado qundo queremos repetir a execução de um bloco de codigo enquanto uma determinada função e verdadeira.

 Exemplos: 
 - Executeuma leitura enquanto um valor não for atingido.
 - Envia email enquanto uma frase não for lida.

"""

if __name__ == "__main__":
    i = 0 

    while i < 10:
        print(i)
        i += 1
       
    print("="*30)

    while i < 20:

        if i > 15:
            break

        i += 1
        print(i)

    print("="*30)

    while i < 40:

        if i % 2 == 0:
            print(f"{i} é par.")
            i += 1
            continue
        
        print(i)
        i += 1
        

