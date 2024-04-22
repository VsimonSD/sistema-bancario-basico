menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

'''

saldo = 0
numero_depositos = 0
limite = 500.00
LIMITE_SAQUES = 3
numero_saques = 0
extrato = ""



while True:

    opcao = input(menu)

    if opcao == 'd':
        print("Favor, informar o valor a ser depositado: ")
        saldo = float(input())

        if saldo <= 0:
            print("favor, informar um valor superior a 0")
        else:
            print(f"Seu saldo atual é de R${saldo}")
            numero_depositos = numero_depositos+1
        
    
    elif opcao == 's':
        print("Favor, informar o quanto você quer sacar: ")
        valor_saque = float(input())

        if numero_saques >= LIMITE_SAQUES:
            print("Você já excedeu a quantidade de saques permitidas no dia!")

        elif valor_saque <= 0:
            print(f"Favor, informar valor superior a 0")

        elif valor_saque > saldo:
            print("Você não tem saldo o suficiente para efetuar o saque")

        elif valor_saque > limite:
            print(f"Você só tem R${limite} de limite para sacar. Favor, informar um valor inferior")
        
        else:
            numero_saques = numero_saques+1
            saldo = saldo - valor_saque
            print(f"Saque efetuado com sucesso, você tem R${saldo} restantes na conta. Você também efetuou {numero_saques} saques de 3.")
    
    elif opcao == 'e':
        if numero_saques > 0 or numero_depositos > 0:
            print(f'''
                    Você realizou {numero_depositos} depósito(s) e efetuou {numero_saques} saque(s).

                    Seu saldo atual é de R${saldo}  

                  ''')
        else:
            print("Você não realizou movimentações! Volte novamente após realizar alguma movimentação")
    
    elif opcao == 's':
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")