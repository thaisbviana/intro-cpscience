a = float(input("a ="))
b = float(input("b ="))
c = float(input("c ="))

import math

delta = (b ** 2) - (4 * a * c)

if delta == 0:
    root1 = (-b + math.sqrt(delta)) / (2 * a)
    print("a raiz desta equação é",root1)
else:
    if delta < 0:
        print("esta equação não possui raízes reais")
    else:
        root1 = (-b + math.sqrt(delta)) / (2 * a)
        root2 = (-b - math.sqrt(delta)) / (2 *a)
        if (root1 > root2):
            print("as raízes da equação são",root2,"e",root1)
        else:
            print("as raízes da equação são",root1,"e",root2)
