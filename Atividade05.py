from abc import ABC, abstractmethod

#classe para registrar o numero de faltas e atrasos do funcionário
class PontoFunc():
    def __init__(self, mes, ano, nroFalta, nroAtrasos):
        self.__mes = mes
        self.__ano = ano
        self.__nroFalta = nroFalta
        self.__nroAtrasos = nroAtrasos

    @property
    def mes(self):
        return self.__mes
    
    @mes.setter
    def mes(self, mes):
        self.__mes = mes
    
    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        self.__ano = ano
    
    @property
    def nroFalta(self):
        return self.__nroFalta
    
    @nroFalta.setter
    def nroFalta(self, nroFalta):
        self.__nroFalta = nroFalta
    
    @property
    def nroAtrasos(self):
        return self.__nroAtrasos
    
    @nroAtrasos.setter
    def nroAtrasos(self, nroAtrasos):
        self.__nroAtrasos = nroAtrasos

    #função para registrar o numero de faltas
    def lancaFaltas(self, nroFalta):
        self.__nroFalta += nroFalta

    #função para registrar o numero de atrasos
    def lancaAtraso(self, nroAtrasos):
        self.__nroAtrasos += nroAtrasos

#classe abstrata que representa os funcionarios
class Funcionario(ABC):
    def __init__(self, codigo, nome):
        self.__codigo = codigo
        self.__nome = nome
        self.__pontoMensalFunc = []

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def pontoMensalFunc(self):
        return self.__pontoMensalFunc
    
    @pontoMensalFunc.setter
    def pontoMensalFunc(self, ponMensalFunc):
        self.__pontoMensalFunc = ponMensalFunc

    #função para adicionar um ponto
    def adicionaPonto(self, mes, ano, faltas, atrasos):
        ponto = PontoFunc(mes, ano, faltas, atrasos)
        self.pontoMensalFunc.append(ponto)

    #função para lançar as faltas do profissional
    def lancaFaltas(self, mes, ano, falta):
        #Neste 'for' se percorre a lista pontoMensalFunc
        for ponto in self.pontoMensalFunc:
            #Este 'if' serve para o ponto localizar o mes e o ano indicado nos
            #paramentros pelas entradas de dados e efetuar a operacao lancaFaltas no mes e ano indicado
            if ponto.mes == mes and ponto.ano == ano:
                ponto.lancaFaltas(falta)

    #funcção para lançar atrasos do profissional
    def lancaAtraso(self, mes, ano, atraso):
        for ponto in self.pontoMensalFunc:
            if ponto.mes == mes and ponto.ano == ano:
                ponto.lancaAtraso(atraso)

    #função para imprimir a folha de ponto do funcionário
    def imprimeFolha(self, mes, ano):
        for ponto in self.pontoMensalFunc:
            if ponto.mes == mes and ponto.ano == ano:
                salarioLiquido = self.calculaSalario(mes, ano)
                bonus = self.calculaBonus(mes, ano)
                print('Código: {}'.format(self.codigo))
                print('Nome: {}'.format(self.nome))
                print('Salário Líquido: {:.2f}'.format(salarioLiquido))
                print('Bonus: {:.2f}'.format(bonus))
    
    #funcao abstrata para calcular o salario
    @abstractmethod
    def calculaSalario(self, mes, ano):
        pass
    
    #funcao abstrata para calcular o bonus
    @abstractmethod
    def calculaBonus(self, mes, ano):
        pass

#classe para representar o professor
class Professor(Funcionario):
    def __init__(self, codigo, nome, titulacao, salarioHora, nroAulas):
        super().__init__(codigo, nome)
        self.__titulacao = titulacao
        self.__salarioHora = salarioHora
        self.__nroAulas = nroAulas

    @property
    def titulacao(self):
        return self.__titulacao
    
    @titulacao.setter
    def titulacao(self, titulacao):
        self.__titulacao = titulacao
    
    @property
    def salarioHora(self):
        return self.__salarioHora
    
    @salarioHora.setter
    def salarioHora(self, salarioHora):
        self.__salarioHora = salarioHora
    
    @property
    def nroAulas(self):
        return self.__nroAulas
    
    @nroAulas.setter
    def nroAulas(self, nroAulas):
        self.__nroAulas = nroAulas

    #funcao para calcular o salario liquido
    def calculaSalario(self, mes, ano):
        for ponto in self.pontoMensalFunc:
            if ponto.mes == mes and ponto.ano == ano:
                faltas = ponto.nroFalta
                return (self.salarioHora * self.nroAulas) - (self.salarioHora * faltas)

    #funcao para calcular o bonus
    def calculaBonus(self, mes, ano):
        for ponto in self.pontoMensalFunc:
            if ponto.mes == mes and ponto.ano == ano:
                atrasos = ponto.nroAtrasos
                #usando a funcao calculaSalario para utilizar o salario liquido
                salarioLiquido = self.calculaSalario(mes, ano)
                bonus = 0.10 * salarioLiquido
                bonus -= (0.01 * atrasos * salarioLiquido)
                return bonus

#funcao para representar os tecnicos administrativos
class TecAdmin(Funcionario):
    def __init__(self, codigo, nome, funcao, salarioMensal):
        super().__init__(codigo, nome)
        self.__funcao = funcao
        self.__salarioMensal = salarioMensal

    @property
    def funcao(self):
        return self.__funcao
    
    @funcao.setter
    def funcao(self, funcao):
        self.__funcao = funcao
    
    @property
    def salarioMensal(self):
        return self.__salarioMensal
    
    @salarioMensal.setter
    def salarioMensal(self, salarioMensal):
        self.__salarioMensal = salarioMensal

    #funcao para calcular o salario liquido
    def calculaSalario(self, mes, ano):
        for ponto in self.pontoMensalFunc:
            if ponto.mes == mes and ponto.ano == ano:
                faltas = ponto.nroFalta
                return (self.salarioMensal) - ((self.salarioMensal / 30) * faltas)

    #funcao para calcular o bonus
    def calculaBonus(self, mes, ano):
        for ponto in self.pontoMensalFunc:
            if ponto.mes == mes and ponto.ano == ano:
                atraso = ponto.nroAtrasos
                salarioLiquido = self.calculaSalario(mes, ano)
                bonus = salarioLiquido * 0.08
                bonus = bonus - (atraso * 0.01 * salarioLiquido)
                return bonus

#Implementação exercida
if __name__ == "__main__":
    
    funcionarios = []

    #Implementando um professor
    prof = Professor(1, "Joao", "Doutor", 45.35, 32)
    prof.adicionaPonto(4, 2021, 0, 0)
    prof.lancaFaltas(4, 2021, 2)
    prof.lancaAtraso(4, 2021, 3)
    funcionarios.append(prof)

    #Implementando um tecnico administrativo
    tec = TecAdmin(2, "Pedro", "Analista Contábil", 3600)
    tec.adicionaPonto(4, 2021, 0, 0)
    tec.lancaFaltas(4, 2021, 3)
    tec.lancaAtraso(4, 2021, 4)
    funcionarios.append(tec)

    #Imprimindo os dois recebendo como parametro o mes e o ano
    for func in funcionarios:
        func.imprimeFolha(4, 2021)
        print()