from datetime import datetime

class Cirurgia():
    def __init__(self, data, paciente, tipoCirurgia):
        self.__data = data
        self.__paciente = paciente
        self.__tipoCirurgia = tipoCirurgia
        self.__equipe = []

    @property
    def data(self):
        return self.__data
    
    @property
    def paciente(self):
        return self.__paciente
    
    @property
    def tipoCirurgia(self):
        return self.__tipoCirurgia
    
    @property
    def equipe(self):
        return self.__equipe
    
    def adicionaProf(self, prof):
        if isinstance(prof, Medico):
            self.equipe.append(prof)
        elif isinstance(prof, Instrumentador):
            self.equipe.append(prof)

    def equipeValida(self):
        instrum  = 0
        cirurgiao = 0
        anest = 0
        for equipe in self.equipe:
            if isinstance(equipe, Instrumentador):
                instrum += 1
            elif isinstance(equipe, Medico):
                if equipe.especialiade == "Cirurgião":
                    cirurgiao += 1
                elif equipe.especialiade == "Anestesista":
                    anest += 1
        if instrum == 0 or cirurgiao == 0 or anest == 0:
            return False
        else:
            return True


    def calculaCustoCir(self):
        if self.equipeValida() == True:
            Valor = 0
            Valor += self.tipoCirurgia.valorCirurgiao
            Valor += self.tipoCirurgia.valorAnest
            Valor += self.tipoCirurgia.valorInstrum
            if self.paciente.tipo == "Particular":
                return Valor
            else: 
                return Valor - (Valor * 0.2)
        else:
            return 0

class Paciente():
    def __init__(self, nome, tipo):
        self.__nome = nome
        self.__tipo = tipo

    @property
    def nome(self):
        return self.__nome
    
    @property
    def tipo(self):
        return self.__tipo
    
class TipoCirurgia():
    def __init__(self, descricao, valorCirurgiao, valorAnest, valorInstrum):
        self.__descricao = descricao
        self.__valorCirurgiao = valorCirurgiao
        self.__valorAnest = valorAnest
        self.__valorInstrum = valorInstrum

    @property
    def descricao(self):
        return self.__descricao
    
    @property
    def valorCirurgiao(self):
        return self.__valorCirurgiao
    
    @property
    def valorAnest(self):
        return self.__valorAnest
    
    @property
    def valorInstrum(self):
        return self.__valorInstrum
    
class ProfSaude():
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome
    
    @property
    def cpf(self):
        return self.__cpf
    
class Medico(ProfSaude):
    def __init__(self, nome, cpf, crm, especialidade):
        super().__init__(nome, cpf)
        self.__crm = crm
        self.__especialidade = especialidade

    @property
    def crm(self):
        return self.__crm
    
    @property
    def especialiade(self):
        return self.__especialidade
    
class Instrumentador(ProfSaude):
    def __init__(self, nome, cpf, coren):
        super().__init__(nome, cpf)
        self.__coren = coren

    @property
    def coren(self):
        return self.__coren


if __name__ == "__main__":
    tipo1 = TipoCirurgia('Oncológica', 8000, 2000, 1000)
    tipo2 = TipoCirurgia('Cardíaca', 9000, 2000, 1200)
    tipo3 = TipoCirurgia('Ortopédica', 7000, 2000, 900)
    pac1 = Paciente('Luiz Silva', 'Particular')
    pac2 = Paciente('José Cruz', 'Convênio')
    pac3 = Paciente('Márcia Reis', 'Particular')
    medCir1 = Medico('Luis Lima', '1234', 'crm1234', 'Cirurgião')
    medCir2 = Medico('Marcos Lopes', '9876', 'crm9876', 'Cirurgião')
    medAnest1 = Medico('Marisa Lins', '4321', 'crm4321', 'Anestesista')
    inst1 = Instrumentador('Ana Souza', '4567', 'coren4567')
    inst2 = Instrumentador('Joel Santos', '7890', 'coren7890')
    cirurgia1 = Cirurgia(datetime(2023, 10, 30), pac1, tipo1)
    cirurgia1.adicionaProf(medCir1)
    cirurgia1.adicionaProf(inst1)
    custo1 = cirurgia1.calculaCustoCir()
    if custo1 == 0:
        print('Equipe não está completa.')
    else:
        print('O valor da cirurgia do paciente {} é {}'.format(pac1.nome, custo1))
    #Saída esperada: 'Equipe não está completa'
    print()    

    cirurgia2 = Cirurgia(datetime(2023, 11, 10), pac2, tipo1)
    cirurgia2.adicionaProf(medCir1)
    cirurgia2.adicionaProf(medAnest1)
    cirurgia2.adicionaProf(inst1)
    custo2 = cirurgia2.calculaCustoCir()
    if custo2 == 0:
        print('Equipe não está completa.')
    else:
        print('O valor da cirurgia do paciente {} é {}'.format(pac2.nome, custo2))
    #Saída esperada: 'O valor da cirurgia do paciente José Cruz é 8800.0'
    print()

    cirurgia3 = Cirurgia(datetime(2023, 11, 20), pac3, tipo2)
    cirurgia3.adicionaProf(medCir1)
    cirurgia3.adicionaProf(medAnest1)
    cirurgia3.adicionaProf(inst2)
    custo3 = cirurgia3.calculaCustoCir()
    if custo3 == 0:
        print('Equipe não está completa.')
    else:
        print('O valor da cirurgia da paciente {} é {}'.format(pac3.nome, custo3))
    #Saída esperada: 'O valor da cirurgia da paciente Márcia Reis é 12200'