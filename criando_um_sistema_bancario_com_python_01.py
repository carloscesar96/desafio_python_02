menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0.0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Digite o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito...R$ {valor:.2f}\n"
        else:
            print("Valor digitado invalido, por favor digite novamente.")

    elif opcao == "2":
        if saldo <= 0 or numero_saques >= 3:
            if saldo <= 0:
                print("Não é possível efetuar o saque, valor insuficiente.")
            else:
                print("Total de saques diários esgotados.")
        else:
            saque = float(input("Qual valor você deseja sacar: "))

            if (saldo - saque) <= 0:
                print("Valor de saque não permitido, saldo insuficiente.")

            else:
                if (saque > 0 and saque <= 500) and (numero_saques <= LIMITE_SAQUES):
                    saldo -= saque
                    extrato += f"Saque......R$ {saque:.2f}\n"
                    numero_saques += 1

                elif (saque > 500) or (saque <= 0):
                    print("Valor de saque não permitido.")

    elif opcao == "3":
        if extrato != "":
            print("\n-------------EXTRATO--------------\n")
            print(extrato)
            print(f"SALDO......R$ {saldo:.2f}")
            print("\n----------------------------------\n")
        else:
            print("\n-------------EXTRATO--------------\n")
            print("Nenhuma operação foi realizada.")
            print("\n----------------------------------\n")

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
