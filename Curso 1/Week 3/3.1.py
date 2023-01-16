#Execuções condicionais e alternativas

#Exercício 3.1
#Dados um número inteiro n, n > 0, e uma sequência com n números inteiros, determinar quantos números da sequência são pares e quantos são ímpares.
#Por exemplo, para a sequência

#6   -2   7   0  -5   8  4
#o seu programa deve escrever o número 4 para o número de pares e 2 para o de ímpares.

count_even = 0
count_odd = 0
insert = input("Add a number to the list?")

while (insert == "yes"):
    n = int(input("Insert number to list:"))
    if (n % 2 == 0):
         count_even = count_even + 1
    else:
        count_odd = count_odd + 1
    insert = input("Do you wish to add numbers to the list?")
    print("Count of even numbers:",count_even,"Cuont of odd numbers:",count_odd)
