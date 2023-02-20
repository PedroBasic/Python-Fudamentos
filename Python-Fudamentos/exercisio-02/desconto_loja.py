if __name__ == "__main__":
    
    produto1 = int(input("Informe o valor do Primeiro Produto: "))
    produto2 = int(input("Informe o valor do Segundo Produto: "))
    produto3 = int(input("Informe o valor do Terceiro Produto: "))

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
    
    texto = f"""
        
        ***************************************
        Desconto na compra de produto acima de:
        ***************************************

        R$ 1000.00  |  R$ 5000.00  | R$ 10000.00 |

        Valor Total: R${soma_produtos}.
        Valor com Desconto: R${desconto}.
        Valor sem Desconto: R${soma_produtos}.

        """

    print(texto)
