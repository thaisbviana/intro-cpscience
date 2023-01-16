def incomodam(n):
	frase = 'incomodam '
	if n<1 or type(n) != int:
		return ""
	elif n==1:
		return frase
	else:
		n-=1
		return frase+incomodam(n)

def elefantes(n):
    primeira_parte = "Um elefante incomoda muita gente\n" + "2 elefantes incomodam incomodam muito mais\n"
    if n == 2:
        return primeira_parte 
    elif n > 2:
        elefantinhos = n
        segunda_parte = str(elefantinhos) + " incomodam muita gente\n" + str(elefantinhos) + " elefantes " + str(incomodam()) + "muito mais\n" + elefantes(n-1)
        return primeira_parte + segunda_parte
    else:
        return ""

print(elefantes(5)) 