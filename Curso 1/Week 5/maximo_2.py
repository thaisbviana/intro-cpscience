def maximo(a,b,c):
    if a > b and a > c:
    	return a
    if b > a and b > c:
        return b
    if c > a and c > b:
        return c
    if a == c and a > b:
        return a
    if a == b and a > c:
        return a
    if b == c and b > a:
        return b
    if a == b == c:
        return a
