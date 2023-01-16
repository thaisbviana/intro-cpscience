def identifica_primos(n):
    prime = True
    i = 2
    while i >= 2 and i < n:
        if n % i == 0:
            prime = False
            return prime
        else:
            i += 1
    return prime

def n_primos(n):
    count = 0
    j = n-1
    while j >= 2 and j < n:
        if identifica_primos(j) == True:
            count += 1
        j -= 1
    return count

n = int(input("Insert your number: "))
print (f"Existem {n_primos(n)} entre 2 e {n}.")
