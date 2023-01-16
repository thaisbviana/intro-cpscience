def ordena(lista):
    end = len(lista)

    for i in range (end - 1):
        posicao_minimo = i
        for j in range (i + 1, end):
            if lista[j] < lista[posicao_minimo]:
                posicao_minimo = j
        
        lista[i], lista[posicao_minimo] = lista[posicao_minimo], lista[i]
    return lista