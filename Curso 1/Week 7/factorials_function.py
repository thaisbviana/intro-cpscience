def factorial(n):
     fact = 1
     while n > 0:
         fact *= n
         n -= 1
     return fact
    
times = int(input('How many times do you wish to insert numbers? '))
while times > 0:
    times -= 1
    n = int(input('Choose your number: '))
    print(factorial(n))
