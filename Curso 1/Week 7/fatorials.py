times = int(input('How many times do you wish to insert numbers? '))
while times > 0:
    times -= 1
    n = int(input('Choose your number: '))
    factorial = 1
    while n > 0:
        factorial *= n
        n -= 1
    print(factorial)
