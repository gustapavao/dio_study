#deposito: valores positivos, armazenados em uma variavél e registrado no extrato
# saque: 3 saques diarios, max 500 reais, respeitado o saldo, registrado também
# extrato: registrar tudo e printar o saldo no final com R$
import datetime

saldo = 0
extrato = ""
limite_diario = 3


while True:
    clique = input('Informe a opção desejada:\n1- Depositar\n2- Sacar\n3- Extrato\n0- Sair\n\t')
    
    if clique == '1':
        try:
            valor_deposito = int(input('Informe o valor do depósito: '))
        except ValueError:
            print('O valor informado é inválido')
        else:
            saldo += valor_deposito
            print('O valor foi depositado.')
            extrato += f'{datetime.datetime.now()} -- Depósito: {valor_deposito}\n'
            
    if clique == '2':
        if limite_diario:
            try:
                valor_saque = int(input('Informe o valor do saque: '))
            except ValueError:
                print('O valor informado é inválido')
            else:
                if saldo >= valor_saque:
                    if valor_saque <= 500:
                        saldo -= valor_saque
                        print('O valor informado foi sacado.')
                        extrato += f'{datetime.datetime.now()} -- Saque: {valor_saque}\n'
                        limite_diario -= 1
                    else:
                        print('Você não pode sacar valores maiores que 500 reais')
                else:
                    print('Você não tem esse valor na sua conta')
                
        else:
            print('Já efetuou 3 saques hoje')
    
    if clique == '3':
        print(extrato)
        print(f"Saldo: R${saldo}")
    if clique == '0':
        break