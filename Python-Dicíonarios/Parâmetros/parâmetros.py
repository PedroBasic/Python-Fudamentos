def imc(peso, altura):
    return peso / (altura * altura)

def pula_linha():
    print("*" * 50)

"""
Menor que 18,5	Magreza
18,5 a 24,9	Normal
25 a 29,9	Sobrepeso
30 a 34,9	Obesidade grau I
35 a 39,9	Obesidade grau II
Maior que 40	Obesidade grau III
"""


if __name__ == "__main__":


    for _ in range(2):

        lista_imc = []

        nome = input("Informe seu Nome: ")
        peso = float(input("Informe se peso: "))
        altura = float(input("Informe sua altura: "))

        resultado = imc(peso, altura)

        if resultado <= 24.9 :
            print(f"{nome}. Seu nivel é Magreza: {resultado:.2f}")
            pula_linha()
        elif resultado >= 25 and resultado < 29.9:
            print(f"{nome}. Parábens você está no peso Normal: {resultado:.2f}")
            pula_linha()
        elif resultado >= 30 and resultado < 34.9:
            print(f"{nome}. Seu nivel de de Obecidade grau I: {resultado:.2f}")

        print(f"{nome}. Seu IMC é: {resultado:.2f}")


        layot = {
            "nome": nome,
            "peso": peso,
            "altura": altura,
            "resultado": resultado
        }

        lista_imc.append(layot)

    for info in lista_imc:
        pula_linha()
        print(f"Nome: {info['nome']}")
        print(f"Peso: {info['peso']}")
        print(f"Altura: {info['altura']}")
        print(f"IMC: {info['resultado']}")

    print(info)



