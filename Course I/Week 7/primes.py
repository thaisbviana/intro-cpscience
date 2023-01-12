def prime(n):
    factor = 2
    if n == 2:
        return True
    while n % factor != 0 and factor < n/2:
        factor += 1
    if n % factor == 0:
        return False
    else:
        return True

n = int(input('Which number do you think is a prime number? '))

while n > 0:
    if prime(n):
        print(f'{n} é primo!')
    else:
        print(f'{n} não é primo!')
    n = int(input('Which number do you think is a prime number? '))
