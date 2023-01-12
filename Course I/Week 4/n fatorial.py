n = int(input("Insert number:"))
fat = 1

if n == 0:
    fat = 1
else:
    for i in range(1,n+1):
        fat = fat * i

print(fat)
