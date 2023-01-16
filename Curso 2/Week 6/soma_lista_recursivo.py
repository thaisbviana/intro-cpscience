def soma_lista(lista):
    inicio = lista[0]

    if len(lista) == 0:
        return False

    if len(lista) == 1:
        return inicio
    else:
        return inicio + soma_lista(lista[1:])