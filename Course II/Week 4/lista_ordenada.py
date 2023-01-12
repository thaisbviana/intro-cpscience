def ordenada(lista):
    ordenacao = True
    for i in lista:
        for j in range(len(lista)-1):
            if lista[j] > lista[j+1]:
                ordenacao = False
    return ordenacao 