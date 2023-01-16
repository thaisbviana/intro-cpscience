vogais = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
alphabet = []
for letra in range(65,91):
    alphabet.append(chr(letra))
for letra in range(97,123):
    alphabet.append(chr(letra))
consoantes = [letra for letra in alphabet if letra not in vogais]

print (alphabet)