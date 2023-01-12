n = int(input("Insert positive integer: "))
prime = True

for i in range(2,n-1):
    if n %  i == 0:
        prime = False

if prime == True:
    print("primo")
else:
    print("não primo")
