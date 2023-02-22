if __name__ == "__main__":
    nt1 = 10
    nt2 = 8
    nt3 = 7
    nt4 = 9
    nt5 = 5

    media = (nt1 + nt2 + nt3 + nt4 + nt5)
    soma_lista = media / 4 

    resultado = (soma_lista - nt1 - nt2)

    if (soma_lista < 5):
        print(f"Voce esta reprovado. {soma_lista}")
    elif(soma_lista >= 6 and soma_lista < 7 ):
        print(f"Você está de recuperação. {soma_lista}")
    elif(soma_lista >= 7):
        print(f"Parabéns você está aprovado. sua media é {soma_lista}")


        texto = f"""
        
        ****************************************************
        Soma das Notas tirando a maior nota e a menor nota.
        ****************************************************

        total media: {soma_lista}
        Resultado tirando a maior e menor nota: {resultado}

        """
    print(texto)