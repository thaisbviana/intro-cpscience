import math

def delta(a,b,c):
    return (b ** 2) - (4 * a * c)

def bhaskara(a,b,c):
    delta(a,b,c)
    if delta(a,b,c) == 0:
        root1 = (-b + math.sqrt(delta(a,b,c))) / (2 * a)
        print("a raiz desta equação é",root1)
    else:
        if delta(a,b,c) < 0:
            print("Esta equação não possui raízes reais.")
        else:
            root1 = (-b + math.sqrt(delta(a,b,c))) / (2 * a)
            root2 = (-b - math.sqrt(delta(a,b,c))) / (2 *a)
    print("As raízes são",root1,"e",root2,".")
