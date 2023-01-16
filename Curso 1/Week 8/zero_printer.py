numbers = []
n = int(input("Insert your number: "))
numbers.append(n)

while n != 0:
    n = int(input("Insert your number: "))
    if n != 0:
        numbers.append(n)

for i in range (1, len(numbers)+1):
     print (numbers[-i])
