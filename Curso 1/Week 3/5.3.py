n = input("Insert number (must be integer, > 0):")
lenght = len(n)
repeat = False

for i in range(0,lenght):
    n[i]
    if (n[i-1]==n[i]):
        repeat = True

if repeat == True:
    print("There is repetition of digit.")
else:
    print("There is no digit repetition.")
