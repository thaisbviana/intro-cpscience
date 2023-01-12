n = input("Insert number: ")
length = len(n)
total = 0

for i in range(0,length):
    total = total + int(n[i])

print(total)
