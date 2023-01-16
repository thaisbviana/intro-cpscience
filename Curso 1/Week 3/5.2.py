n = int(input("Insert number of numbers:"))
crescent_order = True

while crescent_order == True:
    for i in range(0,n):
        number = float(input("Insert number of sequence:"))
        sequence = float(input("Insert sequent number of sequence:"))
        print(number,sequence)
        if (number < sequence):
            crescent_order = True
        elif i == n and crescent_order == True:      
            print("Está em ordem crescente.")
        else:
            crescent_order = False
            print("Não está em ordem crescente.")
            break


