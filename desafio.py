menu = """
[1] saque
[2] Deposito
[3] Extrato
[4] Sair
=>"""
saldo = 3000
saques_feitos= 0 #NUMERO_SAQUES
numero_saque_diario = 3 #Limite saques
limite_saque_diario = 500 #LIMITE
extrato = ""


while True:

    opcao = input(f"Escolha a opção desejada: \n {menu} ")

    if opcao == "1":
        saque = float(input("Informe o valor de saque: "))

        excedeu_saldo = saque > saldo
        excedeu_limite = saque > limite_saque_diario
        excedeu_saque = numero_saque_diario >= limite_saque_diario

        if excedeu_saque:
            
                print("Quantidade de saque diário excedido")
    
        elif excedeu_limite:
         
                print("Limite de saque excedido! Tente novamente amanhã! Obrigado.")
    
    
        
        if excedeu_saldo:
                 print("Operação falhou! Saldo insuficiente!")

        elif saque > 0:
            saldo -= saque
            extrato += f"saque: R$ {saque:.2f}\n"
            numero_saque_diario +=1
            print("Saque sendo realizado, retire o dinheiro no local indicado")

    
    if opcao == "3": 
        print("Exibindo o extrato ...")
        print("{extrato}")
        print(f"\n Saldo: R$ {saldo:.2f}")
    


    if opcao == "2":
        print("Deposito")
        valor = float(input("Informe um valor para depósito: "))

        if valor > 0: 
         saldo += valor
         extrato += f"Deposito: R$ {valor: .2f}"
        else:
            print("Operação falhou! o valor informado não é válido!")

    elif opcao == "4":
        print("Saindo.. Até logo!")
        break
else:
     print("Operação inválida, por favor selecione novamente a operação desejada.")


    