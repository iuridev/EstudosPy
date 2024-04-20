

saldo = 0
limite = 500
extrato : str
extrato = ""
numero_depositos = 0
numero_saques = 0
LIMITE_SAQUES = 3

def menu():
    menu = menu = """
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair

        => """
    return input(menu)

def depositar(valor, saldo, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += str(f"Depósito: R$ {valor:.2f}\n")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, valor
    

def sacar(saldo, dvalor, eextrato, limite, numero_saques, LIMITE_SAQUES):
    
    excedeu_saldo = dvalor > saldo
    excedeu_limite = dvalor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES


    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
            saldo -= valor
            #eextrato += f"Saque: R$ {valor:.2f}\n"
            bug = list(f"Saque: R$ {valor:.2f}\n")
            eextrato = eextrato + bug
            numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, eextrato

def extrair(saldo):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")  


while True:
    opcao_escolhida = menu()

    if opcao_escolhida == 'd':
        valor = float(input('Digite o valor para deposito: R$'))
        saldo, extrato = depositar(valor, saldo, extrato)

    elif opcao_escolhida == 's':
        valor = float(input('Digite o valor para saque: R$'))
        saldo, extrato = sacar(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES)
        
    elif opcao_escolhida == 'e':
        extrair(saldo)
    
    elif opcao_escolhida == 'q':
        print("Finalizando o Sistema.")
        break
    else:
        print("Opção inválida!")

