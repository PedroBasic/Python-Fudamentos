if __name__ == "__main__":

    lista_cliente = []
    qtd_sexo_m = 0
    qtd_sexo_f = 0
    idade_total = 0

    for _ in range(5):

        nome = input("Informe seu Nome: ")
        idade = int(input("Informe sua idade: "))
        sexo = input("Informe seu sexo: 'M' OU 'F': ")

        print(nome)

        if sexo == 'M':
            qtd_sexo_m = qtd_sexo_m + 1
        else:
            qtd_sexo_f = qtd_sexo_f + 1

        txt = {

        "nome": nome,
        "idade": idade,
        "sexo": sexo

        }

        lista_cliente.append(txt)

    for cliente in lista_cliente:
        print(f"Nome: {cliente['nome']}")
        print(f"Idade: {cliente['idade']}")
        print(f"Sexo: {cliente['sexo']}")

        print(f"Valor media idades: {idade_total / len(lista_cliente)}")
        print(f"Quatidade sexo Masculino {qtd_sexo_m}")
        print(f"Quantidade sexo Feminino: {qtd_sexo_f}")

        print(cliente)

        