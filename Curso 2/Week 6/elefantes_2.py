def incomodam(n):
    if n <= 0:
        return ""
    elif n == 1:
        return "incomodam "
    else:
        return "incomodam " + incomodam(n-1)

def elefantes(n):
    if n <= 1:
        return ""
    elif n == 2:
        return "Um elefante incomoda muita gente\n" + "2 elefantes incomodam incomodam muito mais\n"
    else:
        return elefantes(n-1) + str(n-1) + " elefantes incomodam muita gente\n" + str(n) + " elefantes " + incomodam(n) + "muito mais\n"