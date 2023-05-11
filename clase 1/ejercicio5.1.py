nota = int(input(" ingrese una nota 0-10: "))

while nota < 0 or nota > 10:
    nota = int(input(" ingrese una nota entre 0-10 pf "))

print(f" gracias tu nota es: {nota}" )