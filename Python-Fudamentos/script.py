if __name__ == "__main__":

    SALARIO_FIXO = 1000
    comissao = 0
    valor_total = 0
    valor_vendido = int(input("Informe o valor vendido: "))

    if (valor_vendido > 1000 and valor_vendido <= 50000):
        comissao = valor_vendido * 0.01
        print(f"O funcionario vai receber 10% de comissao R${comissao}. ")
    elif(valor_vendido > 20000 and valor_vendido <= 100000):
        comissao = valor_vendido * 0.02
        print(f"O funcionario vai receber 20% da comissão R${comissao}. ")
    elif(valor_vendido > 100000 and valor_vendido <= 200000):
        comissao = valor_vendido * 0.03
        print(f"O funcionario vai receber uma comissão de 30% R${comissao}. ")

        valor_total = SALARIO_FIXO + comissao
    
    texto = f"""

    *****************************
    Comissão do Funcionario
    *****************************

    Salario fixo = R${SALARIO_FIXO}.
    Valor Vendido = R${valor_vendido}.
    Valor comissão = R${comissao}.

    Valor Total = R${valor_total}.
    
    """

    print(texto)