a = int(input('Digite a altura: '))
l = int(input('Digite a largura: '))

z = l
while z >= 1:
    y = a
    while y >= 1:
        if y == a or y == 1:
            print("#", end="")
        elif z == l or z ==1:
            print("#", end="")
        else:
            print(" ", end="")
        y -= 1
    print()
    z -= 1
