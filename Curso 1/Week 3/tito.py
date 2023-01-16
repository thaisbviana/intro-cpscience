n = int(input("Insert your number:"))
start_n = 1
triangular = False
seq = int((start_n * (start_n + 1) * (start_n + 2)))


while (seq <= n):
    if (seq == n):
        triangular = True
    start_n = start_n + 1

if triangular == True:
    print("O número",n,"é triangular.")
else:
    print("O número",n,"não é triangular.")
