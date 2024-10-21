from abc import ABC, abstractmethod

class EmpDomestica(ABC):
    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefone = telefone

    @property
    def nome(self):
        return self.__nome
    
    @property
    def telefone(self):
        return self.__telefone
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    
    @abstractmethod
    def getSalario(self):
        pass

class Horista(EmpDomestica):
    def __init__(self, nome, telefone, horasTrabalhadas, valorPorHora):
        super().__init__(nome, telefone)
        self.__horasTrabalhadas = horasTrabalhadas
        self.__valorPorHora = valorPorHora
    
    @property
    def horasTrabalhadas(self):
        return self.__horasTrabalhadas
    
    @property
    def valorPorHora(self):
        return self.__valorPorHora
    
    def getSalario(self):
        return self.horasTrabalhadas * self.valorPorHora
    

class Diarista(EmpDomestica):
    def __init__(self, nome, telefone, diasTrabalhadas, valorPordia):
        super().__init__(nome, telefone)
        self.__diasTrabalhadas = diasTrabalhadas
        self.__valorPordia = valorPordia
    
    @property
    def diasTrabalhadas(self):
        return self.__diasTrabalhadas
    
    @property
    def valorPordia(self):
        return self.__valorPordia
    
    def getSalario(self):
        return self.diasTrabalhadas * self.valorPordia

class Mensalista(EmpDomestica):
    def __init__(self, nome, telefone, valorMensal):
        super().__init__(nome, telefone)
        self.__valorMensal = valorMensal
    
    @property
    def valorMensal(self):
        return self.__valorMensal
    
    def getSalario(self):
        return self.valorMensal
    
if __name__ == "__main__":
    horista = Horista('Ana', '99999-9999', 160, 12)
    diarista = Diarista('Marcela', '88888-8888', 20, 65)
    mensalista = Mensalista('Adriana', '77777-7777', 1200)

    horista.nome = 'Maria'
    

    empregadas = [horista, diarista, mensalista]
    for empregada in empregadas:
        print('Nome: {} - Salário: {}'.format(empregada.nome, empregada.getSalario()))

    maisBarata = empregadas[0]

    for empregada in empregadas[1:]:
      if empregada.getSalario() < maisBarata.getSalario():
        maisBarata = empregada
    
    print('\nOpção mais barata: {} - Telefone: {} - Salário: R${}'.format(maisBarata.nome, maisBarata.telefone, maisBarata.getSalario()))