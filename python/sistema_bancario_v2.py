#criar funções para o que já existe e criar duas novas
import datetime

saldo = 0
extrato = ""
limite_diario = 3
usuarios = []
contas_bancarias = []
quantidade_de_contas = 0

def depositar(valor:int, saldo:vars, extrato): 
    try:
        valor_deposito = int(valor)
    except ValueError:
        print('O valor informado é inválido')
    else:
        saldo += valor_deposito
        extrato += f'{datetime.datetime.now()} -- Depósito: {valor_deposito}\n'
        return f'O valor de R${valor} reais foi depositado com sucesso.\nO seu novo saldo é de R${saldo} reais'
            
def sacar(valor, saldo, extrato, limite_diario=limite_diario):
    if limite_diario:
        try:
            valor_saque = int(valor)
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
    
def ver_extrato():
    print(extrato)
    print(f"Saldo: R${saldo}")

def verificar_cpf(cpf):
    for i in usuarios:
        for key, values in i.items():
            if cpf == values:
                return False
    return True

def criar_usuario(nome, cpf, rua, numero, bairro,cidade,sigla_estado):
    if str(cpf).isnumeric():
        cpf = int(cpf)
    else:
        cpf = str(cpf).replace("-","")
        cpf = str(cpf).replace(".","")
        cpf = int(cpf)
    if verificar_cpf(cpf):
        usuarios.append({'nome':nome, 'cpf': cpf, 'endereço':f'{rua}, {numero}, {bairro}, {cidade}/{sigla_estado}'})
    else:
        print('Já existe um usuário com esse CPF')

def criar_conta(agencia='0001', numero_conta, cpf):
    if str(cpf).isnumeric():
        cpf = int(cpf)
    else:
        cpf = str(cpf).replace("-","")
        cpf = str(cpf).replace(".","")
        cpf = int(cpf)
    if verificar_cpf(cpf):
        contas_bancarias.append({'agencia': agencia, 'numero da conta': numero_conta, 'usuario':cpf})
    else:
        print(f'O usuário {cpf} não está registrado no nosso banco')


    

    

print(usuarios)