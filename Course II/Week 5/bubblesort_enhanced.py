#funciona melhor para listas quase ordenadas(?)
def bolha (lista):
    end = len(lista)
    
    for i in range(end-1, 0, -1):
        trocou = False
        for j in range(i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                trocou = True
        if not trocou:
            return lista
    
    return lista