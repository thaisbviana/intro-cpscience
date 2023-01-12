def busca(lista, elemento):
    if elemento in lista:
        for i in range(len(lista)):
            if elemento == lista[i]:
                return i
    else:
        return False