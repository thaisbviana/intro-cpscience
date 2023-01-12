def maiusculas(frase):
    character = ""
    for letter in frase:
        if letter >= "A" and letter <= "Z":
            character = character + letter
    return character