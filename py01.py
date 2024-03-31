#Atividade da FACULADE
# Calculo de IMC

peso = float(input("Informe o seu peso: "))
altura = float(input("Informe a sua altura:"))

imc = peso / altura ** 2

print(f"O seu IMC é {imc}")

if imc < 18.5:
    print("CUIDADO! CLASSIFICAÇÃO: MAGREZA")
elif imc < 24.9:
    print("PARABÉNS! CLASSIFICAÇÃO: NORMAL")
elif imc < 29.9:
    print("CUIDADO! CLASSIFICAÇÃO: SOBREPESO")
elif imc < 39.9:
    print("CUIDADO! CLASSIFICAÇÃO: OBESIDADE")
else:
    print("CUIDADO! CLASSIFICAÇÃO: OBESIDADE GRAVE")