listaValores = []
contiue = ''.upper()

while contiue != 'n':
    
    digite = int(input("Informe um número: "))
    
    if not digite in listaValores:
        listaValores.append(digite)
        print('Valor Adicionado com sucesso ...')
    else:
        print('Ops! Valor duplicado ...')
        
    contiue = str(input("Deseja continuar [S/N]: "))


listaValores.sort()
print(listaValores)
 