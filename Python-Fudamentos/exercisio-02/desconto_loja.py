if __name__ == "__main__":
    
    nome_produto1 = input("Informe o nome do Primeiro Produto: ")
    produto1 = float(input("Informe o valor do Primeiro Produto: "))

    nome_produto2 = input("Informe o nome do Segundo Produto: ")
    produto2 = float(input("Informe o valor do Segundo Produto: "))
    
    nome_produto3 = input("Informe o nome do Terceiro Produto: ")
    produto3 = float(input("Informe o valor do Terceiro Produto: "))

    desconto = 0
    soma_produtos = (produto1 + produto2 + produto3)
    valor_desconto = 0

    if (soma_produtos >= 1000 and soma_produtos < 5000):
        desconto = soma_produtos * 0.1
        print(f"Parabéns voce recebeu 10%. ")

    elif(soma_produtos >= 5000 and soma_produtos < 10000):
        desconto = soma_produtos * 0.2
        print(f"Parabéns você ganhou 20%. ")

    elif(soma_produtos >= 10000):
        desconto = soma_produtos * 0.3
        print(f"Voce ganhou um super desconto de 30%. ")

    elif(soma_produtos < 1000):
        print(f"Você não ganhou nenhum desconto.")
    

    valor_desconto = soma_produtos - desconto

    texto = f"""
        
        ***************************************
        Desconto na compra de produto acima de:
        ***************************************

        R$ 1000.00  |  R$ 5000.00  | R$ 10000.00 |

        Valor Total: R${soma_produtos:.2f}.
        Valor com Desconto: R${desconto:.2f}.
        Valor sem Desconto: R${soma_produtos:.2f}.
        Valor descontado: R${valor_desconto:.2f}

        ***************************************
        Produtos Comprados.
        ***************************************

        Nome Produto: {nome_produto1}  Valor Produto: R${produto1:.2f}.
        ----------------------------------------------------------
        Nome Produto: {nome_produto2}  Valor Produto: R${produto2:.2f}.
        ----------------------------------------------------------
        Nome Produto: {nome_produto3}  Valor Produto: R${produto3:.2f}.


        """

    print(texto)
    