class Veiculo:
    def __init__(self, marca, cor, motorLigado):
        self.__marca = marca
        self.__cor = cor
        self.__motorLigado = motorLigado

    def getMarca(self):
        return self.__marca
    
    def getCor(self):
        return self.__cor
    
    def ismotorLigado(self):
        return self.__motorLigado

    def ligaMotor(self):
        if self.__motorLigado == True:
            print('Motor já está ligado')
        else:
            self.__motorLigado == True
            print('Motor ligado')
    
    def desligaMotor(self):
        if self.__motorLigado == True:
            self.__motorLigado == False
            print('Motor desligado')
        else:
            print('Motor já desligado')

class Carro(Veiculo):
    def __init__(self, marca, cor, motorLigado, portaMalasCheio):
        #chama o construtor da superclasse    
        super().__init__(marca, cor, motorLigado)
        self.__portaMalasCheio = portaMalasCheio

    def isPortaMalasCheio(self):
        return self.__portaMalasCheio

    def enchePortaMalas(self):
        if self.__portaMalasCheio == True:
            print('O porta malas já está cheio')
        else:
            self.__portaMalasCheio == True
            print('Porta malas enchido')

    def esvaziaPortaMalas(self):
        if self.__portaMalasCheio == True:
            self.__portaMalasCheio == False
            print('Porta malas esvaziado')
        else:
            print('Porta malas já vazio')

    def mostraAtributos(self):
        print('Este carro é um {} {}'.format(self.getMarca(), self.getCor()))
        if(self.ismotorLigado()):
            print('Seu motor esta ligado')
        else:
            print('Seu motor esta desligado')
        if(self.isPortaMalasCheio()):
            print('Seu porta malas esta cheio')
        else:
            print('Seu porta malas esta vazio')

class Motocileta(Veiculo):
    def __init__(self, marca, cor, motorLigado, estilo):
        super().__init__(marca, cor, motorLigado)
        self.__estilo = estilo

    def getEstilo(self):
        return self.__estilo
    
    def mostraAtributos1(self):
        print('Esta motocicleta é uma {} {} de estilo {}'.format(self.getMarca(), self.getCor(), self.__estilo))

        if (self.ismotorLigado()):
            print('O motor esta ligado')
        else:
            print('O motor esta desligado')

if __name__ == "__main__":
    m = Motocileta('Honda', 'azul', False, 'naked')
    m.mostraAtributos1()
    m.ligaMotor()
    m.mostraAtributos1()
    print('')

    c = Carro('Fiat', 'branco', True, False)
    c.mostraAtributos()
    c.desligaMotor()
    c.enchePortaMalas()
    c.mostraAtributos()