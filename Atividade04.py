from abc import ABC, abstractmethod

class Terreno(ABC):
    def __init__(self, localizacao, preco):
        self.__localizacao = localizacao
        self.__preco = preco

    @property
    def localizacao(self):
        return self.__localizacao
    
    @property
    def preco(self):
        return self.__preco
    
    @localizacao.setter
    def localizacao(self, localizacao):
        self.__localizacao = localizacao

    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    @abstractmethod
    def calcula_peso(self):
        pass

class TerrenoCircular(Terreno):
    def __init__(self, localizacao, preco, raio):
        super().__init__(localizacao, preco)
        self.__raio = raio
    
    @property
    def raio(self):
        return self.__raio
    
    def calcula_peso(self):
        return self.preco / ((self.raio * self.raio) * 3.14)
    

class TerrenoRetangular(Terreno):
    def __init__(self, localizacao, preco, ladoMenor, ladoMaior):
        super().__init__(localizacao, preco)
        self.__ladoMenor = ladoMenor
        self.__ladoMaior = ladoMaior

    @property
    def ladoMenor(self):
        return self.__ladoMenor
    
    @property
    def ladoMaior(self):
        return self.__ladoMaior
    
    def calcula_peso(self):
        return self.preco / (self.ladoMaior * self.ladoMenor)
    
    
if __name__ == "__main__":

    circular = TerrenoCircular('Bairro Morro Chique', 70000, 15)
    retangular = TerrenoRetangular('Bairro das Laranjeiras', 75000, 20, 35)
    circular2 = TerrenoCircular('Bairro Vila Rubens', 110000, 20)

    terrenos = [circular, retangular, circular2]
    for terreno in terrenos:
        print('Localização: {}  -  Preço: {:.2f}  -  Peso: {:.2f}'.format(terreno.localizacao, terreno.preco, terreno.calcula_peso()))

    melhorCusto = terrenos[0]

    for terreno in terrenos[1:]:
        if terreno.calcula_peso() < melhorCusto.calcula_peso():
            melhorCusto = terreno
    
    print('\nO terreno com melhor custo por área quadrada é o:\nLocalização: {}\nPreço: {}\nPeso: {}'.format(melhorCusto.localizacao, melhorCusto.preco, melhorCusto.calcula_peso()))