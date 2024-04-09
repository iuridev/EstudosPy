opcao = -1

while opcao != 0:
    opcao = int(input("Digite: \n [1] - Sacar \n [2] - Extrato \n [0] - Sair\n: "))
    if opcao == 1:
        print("Sacando ... \n")
    elif opcao == 2:
        print("Exibindo extrato ...")


#outra forma de usar o While:
        
while True:
    numero = int(input("Digite um número:"))
    if numero % 2 == 1:
        print(f"numero impa: {numero}, parar o programa.")
        break
    else:
        print(f"numero par: {numero}, continuar o programa.")