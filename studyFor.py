texto = input("Digite uma Palavra: ")

VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="-")
else:
    print()


#outro uso do FOR:
for numero in range(0,11):
    print(numero, end=" ")

#outro uso do FOR:
for numero in range(0, 50, 5):
    print(numero, end=" ")