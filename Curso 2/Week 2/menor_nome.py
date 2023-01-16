def menor_nome(nomes):
    shortest = nomes[0]
    for i in nomes:
        if len(shortest.strip()) > len(i.strip()):
            shortest = i.strip()
    return shortest.capitalize()