if __name__ == "__main__":
    
    lista_cursos = ["Java", "Python", "MySql", "Oracle", "PHP"]
    nova_lista = lista_cursos

    nova_lista.pop(-1)

    print(nova_lista)
    print(lista_cursos)

    lista_verao = lista_cursos.copy()
    lista_verao.append("PHP")

    print(lista_verao)
    print(nova_lista)
    print(lista_cursos)

    lista_primavera = lista_verao[:]
    lista_primavera.append("Angular")

    print(lista_cursos)
    print(nova_lista)
    print(lista_verao)
    print(lista_primavera)