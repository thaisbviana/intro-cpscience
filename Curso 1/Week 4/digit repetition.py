n = input("Insert number (must be integer, > 0):")
lenght = len(n)
repeat = False

for i in range(1,lenght):
    n[i]
    if (n[i-1]==n[i]):
        repeat = True

if repeat == True:
    print("sim")
else:
    print("não")
