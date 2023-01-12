n = input("Insert value (must be >= 0):")
d = input("Insert desired digit (must be between 0 and 9):")
counter = 0
length = len(n)
i = 0

while i <=(length -1):
    if format(n[i])== d:
        counter = counter + 1
    i = i + 1

print ("O dígito",d,"ocorre",counter,"vezes em",n)
