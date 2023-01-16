p1_x = float(input("Coordenada do ponto 1 - abscissa:"))
p1_y = float(input("Coordenada do ponto 1 - ordenada:"))
p2_x = float(input("Coordenada do ponto 2 - abscissa:"))
p2_y = float(input("Coordenada do ponto 2 - ordenada:"))

import math
d = math.sqrt (((p1_x - p2_x) ** 2) + ((p1_y - p2_y) ** 2))

if (d >= 10):
    print("longe")
else:
    print("perto")
