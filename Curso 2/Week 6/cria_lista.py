def cria_lista(n):
    list_int = []
    count = 0
    while n > 0:
        count += 1
        list_int.append(count)
        n = n - 1
    return list_int