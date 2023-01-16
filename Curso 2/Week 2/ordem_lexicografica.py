# Escreva uma função que recebe array de strings como parâmetro e devolve o primeiro string na ordem lexicográfica, ignorando-se letras maiúsculas e minúsculas. O primeiro na ordem lexicográfica não é o primeiro elemento do array; é o primeiro na ordem lexicográfica, aquele que tem as letras com ord menor, então se tiver uma palavra que começa com a, vai vir antes que uma palavra que começa com b.
def primeiro_lex(lista):
    primeira_palavra = lista[0]
    for palavra in lista:
        if ord(palavra.strip()[0]) < ord(primeira_palavra.strip()[0]):
            primeira_palavra = palavra
    return primeira_palavra