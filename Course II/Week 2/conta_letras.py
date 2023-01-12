def conta_letras(frase, contar="vogais"):
    vogais = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    alphabet = []
    for letra in range(65,91):
        alphabet.append(chr(letra))
    for letra in range(97,123):
        alphabet.append(chr(letra))
    consoantes = [letra for letra in alphabet if letra not in vogais]
    count_vogais = 0
    count_consoantes = 0
    for letra in frase:
        if letra in vogais:
            count_vogais += 1
        elif letra in consoantes:
            count_consoantes += 1
    if contar == "vogais":
        return count_vogais
    if contar == "consoantes":
        return count_consoantes