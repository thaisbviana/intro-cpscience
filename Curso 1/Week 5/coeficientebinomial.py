def fatorial(a):
    fat = 1
    for i in range(1,a+1):
        fat = fat * i
    return fat

def coeficientebinomial(n,k):
    coef = fatorial(n)/(fatorial(k) * fatorial(n-k))
    return coef
