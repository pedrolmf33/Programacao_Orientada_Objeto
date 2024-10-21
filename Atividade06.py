from abc import ABC
from datetime import date

class Conta():
    def __init__(self, nome, nroConta, limite, senha):
        self.__nroConta = nroConta
        self.__nome = nome
        self.__limite = limite
        self.__senha = senha

        self.__transacoes = []
    
    @property
    def nroConta(self):
        return self.__nroConta

    @property
    def nome(self):
        return self.__nome

    @property
    def limite(self):
        return self.__limite
    
    @property
    def senha(self):
        return self.__senha
    
    @property
    def transacoes(self):
        return self.__transacoes
    
    def adicionaDeposito(self, valor, data, nomeDepositante):
        deposito = Deposito(valor, data, nomeDepositante)
        return self.__transacoes.append(deposito)

    def adicionaSaque(self, valor, data, senha):
        if senha != self.__senha:
            return False
    
        if self.calculaSaldo() + self.limite >= valor:
            saque = Saque(valor, data, senha)
            self.__transacoes.append(saque)
            return True
        else:
            return False

    def adicionaTransf(self, valor, data, senha, contaFavorecido):
        if senha != self.senha or self.calculaSaldo() + self.limite < valor:
            return False
        
        transferenciaDebito = Transferencia(valor, data, senha, "D")
        self.transacoes.append(transferenciaDebito)

        transferenciaCredito = Transferencia(valor, data, senha, "C")
        contaFavorecido.transacoes.append(transferenciaCredito)

        return True

    def calculaSaldo(self):
        total = 0
        for transacao in self.transacoes:
            if isinstance(transacao, Deposito):
                total += transacao.valor
            elif isinstance(transacao, Saque):
                total -= transacao.valor
            elif isinstance(transacao, Transferencia):
                if transacao.tipoTransf == "C":
                    total += transacao.valor
                elif transacao.tipoTransf == "D":
                    total -= transacao.valor
        return total + self.limite

class Transacao(ABC):
    def __init__(self, valor, data):
        self.__valor = valor
        self.__data = data

    @property
    def valor(self):
        return self.__valor
    
    @property
    def data(self):
        return self.__data
    
class Saque(Transacao):
    def __init__(self, valor, data, senha):
        super().__init__(valor, data)
        self.__senha = senha
    
    @property
    def senha(self):
        return self.__senha
    

class Deposito(Transacao):
    def __init__(self, valor, data, nomeDepositante):
        super().__init__(valor, data)
        self.__nomeDepositante = nomeDepositante

    @property
    def nomeDepositante(self):
        return self.__nomeDepositante
    

class Transferencia(Transacao):
    def __init__(self, valor, data, senha, tipoTransf):
        super().__init__(valor, data)
        self.__senha = senha
        self.__tipoTransf = tipoTransf

    @property
    def senha(self):
        return self.__senha
    
    @property
    def tipoTransf(self):
        return self.__tipoTransf
    
if __name__ == "__main__":
 c1 = Conta(1234, 'Jose da Silva', 1000, 'senha1')
 c1.adicionaDeposito(5000, date.today(), 'Antonio Maia')
 if c1.adicionaSaque(2000, date.today(), 'senha1') == False:
    print('Não foi possível realizar o saque no valor de 2000')
 if c1.adicionaSaque(1000, date.today(), 'senha-errada') == False: # deve falhar
    print('Não foi possível realizar o saque no valor de 1000')

 c2 = Conta(4321, 'Joao Souza', 1000, 'senha2')
 c2.adicionaDeposito(3000, date.today(), 'Maria da Cruz')
 if c2.adicionaSaque(1500, date.today(), 'senha2') == False:
    print('Não foi possível realizar o saque no valor de 1500')
 if c2.adicionaTransf(5000, date.today(), 'senha2', c1) == False: # deve falhar
    print('Não foi possível realizar a transf no valor de 5000')
 if c2.adicionaTransf(800, date.today(), 'senha2', c1) == False:
    print('Não foi possível realizar a transf no valor de 800')

 print('--------')
 print('Saldo de c1: {}'.format(c1.calculaSaldo())) # deve imprimir 4800
 print('Saldo de c2: {}'.format(c2.calculaSaldo())) # deve imprimir 1700