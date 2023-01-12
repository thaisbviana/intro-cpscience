import random

def lista_grande(n):
    lista=[]
    for i in range(n):
        lista.append(random.randint(-n,n))
    
    return lista