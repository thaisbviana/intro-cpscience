import math

def e_hipotenusa(n):

    isHipotenusa= False
    j=1

    for j in range(1,n,1):

        i=1    
        for i in range(1,n,1):

            x = math.sqrt((i**2+j**2))
            
#            print(f"i={i} j={j} x={x}")
            
            if x==n:

                isHipotenusa=True

    return isHipotenusa


def soma_hipotenusas(n):

    soma=0
    
    for y in range(1, n+1, 1):

        if e_hipotenusa(y)==True:

            soma+=y
            
    return soma
