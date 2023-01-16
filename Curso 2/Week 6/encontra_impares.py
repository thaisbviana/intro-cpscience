def encontra_impares(lista):
    odd_numbers = []
    if not lista:
        return []
    if lista[0] % 2 != 0:
        odd_numbers.insert(lista[0],-1)
        return [lista[0]] + encontra_impares(lista[1:])
    return encontra_impares(lista[1:])