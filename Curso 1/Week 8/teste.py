def soma_elementos(lista):
    soma = 0
    for i in lista:
        soma = soma + lista[i-1]
    return soma

lista = [1,2,3,4]
print(soma_elementos(lista))
