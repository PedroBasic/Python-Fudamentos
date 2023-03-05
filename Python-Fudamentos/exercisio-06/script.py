"""
Gere números randomicos de 0 a 50 e mostre seu valor max() e valor min();
"""

from random import randint

if __name__ == "__main__":
    
    lista_num = [randint(0, 50) for _ in range(50)]
    print(f"O meaior número dessa lista é {max(lista_num)}.")
    print(f"O menor valor dessa lista é {min(lista_num)}. ")


    