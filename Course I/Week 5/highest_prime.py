def primo(n):
    primo = True
    for i in range(2,n):
        if n % i == 0:
            primo = False
    return primo


def maior_primo(n):
    while primo(n) == False:
        n-=1
    return n
            

        
