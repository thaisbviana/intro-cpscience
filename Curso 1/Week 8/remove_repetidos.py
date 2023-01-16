def remove_repetidos(lista):
    n = []
    for i in lista:
        if i not in n:
            n.append(i)
    n.sort()
    return n