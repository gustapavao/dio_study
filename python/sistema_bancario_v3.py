import datetime
from abc import ABC, abstractclassmethod, abstractproperty

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
class Conta:
    def __init__(self, numero, cliente):
        self.__saldo = 0
        self.__numero = numero
        self.__agencia = "0001"
        self.__cliente = cliente
        self.__historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self.__saldo

    @property
    def numero(self):
        return self.__numero
    
    @property
    def agencia(self):
        return self.__agencia
    
    @property
    def cliente(self):
        return self.__cliente
    
    @property
    def historico(self):
        return self.__historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print('Você não tem saldo suficiente para realizar esta operação')

        elif valor > 0:
            self.__saldo -= valor
            print(f'Saque realizado no valor de {valor}')
            return True
        else:
            print('Operação falhou')
        return False
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print("\nDepósito realizado com sucesso")
            return True
        else:
            print('Operação falhou')
            return False

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saque=3):
        super().__init__(numero, cliente)
        self.__limite = limite
        self.__limite_saques = limite_saque

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes 
             if transacao ['tipo'] == Saque.__name__]
        )

        excedeu_limite = valor > self.__limite
        excedeu_saques = numero_saques >= self.__limite_saques

        if excedeu_limite:
            print('Excedeu valor limite')
        
        elif excedeu_saques:
            print('Excedeu limite de saques')

        else:
            return super().sacar(valor)
        
        return False
    
    def __str__ (self):
        return f"""
            Agência:\t{self.agencia}
            C/C:\t{self.numero}
            Titular:\t{self.cliente.nome}

        """
class Historico:
    def __init__(self):
        self.__transacoes = []

        @property
        def transacoes(self):
            return transacoes
        
        def adicionar_transacao(self, transacao):
            self.__transacoes.append(
                    {
                        "tipo": transacao.__class__.__name__,
                        "valor": transacao.valor,
                        "data": datetime.datetime.now().strftime
                        ("%d-%m-%Y %H:%M:%s"),
                    }
            )
class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass
    @abstractclassmethod
    def resgistrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor
    
    def registrar(self,conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)