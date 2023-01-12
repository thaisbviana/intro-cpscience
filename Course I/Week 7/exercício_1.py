a = int(input('Digite a altura: '))
l = int(input('Digite a largura: '))

while l >= 1:
    y = a
    while y >= 1:
        print("#", end="")
        y -= 1
    print()
    l -= 1
