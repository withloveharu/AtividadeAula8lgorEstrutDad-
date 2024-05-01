from abc import ABC, abstractmethod

class Categoria:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

class Produto(ABC):
    def __init__(self, modelo, cor, preco, categoria):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self.categoria = categoria

    def getInformacoes(self):
        return {
            "modelo": self.modelo,
            "cor": self.cor,
            "preco": self.preco,
            "categoria_id": self.categoria.id,
            "categoria_nome": self.categoria.nome
        }

    @abstractmethod
    def cadastrar(self):
        pass

class Desktop(Produto):
    def __init__(self, modelo, cor, preco, categoria, potenciaDaFonte):
        super().__init__(modelo, cor, preco, categoria)
        self._potenciaDaFonte = potenciaDaFonte

    def getInformacoes(self):
        info = super().getInformacoes()
        info["potencia_da_fonte"] = self._potenciaDaFonte
        return info

    def getPotenciaDaFonte(self):
        return self._potenciaDaFonte

    def setPotenciaDaFonte(self, potencia):
        self._potenciaDaFonte = potencia

    potenciaDaFonte = property(getPotenciaDaFonte, setPotenciaDaFonte)

    def cadastrar(self):
        pass

class Notebook(Produto):
    def __init__(self, modelo, cor, preco, categoria, tempoDeBateria):
        super().__init__(modelo, cor, preco, categoria)
        self.__tempoDeBateria = tempoDeBateria

    def getInformacoes(self):
        info = super().getInformacoes()
        info["tempo_de_bateria"] = self.__tempoDeBateria
        return info

    # Getter e Setter para o atributo tempoDeBateria
    def getTempoDeBateria(self):
        return self.__tempoDeBateria

    def setTempoDeBateria(self, tempo):
        self.__tempoDeBateria = tempo

    tempoDeBateria = property(getTempoDeBateria, setTempoDeBateria)

    def cadastrar(self):
        pass

if __name__ == "__main__":
    categoria1 = Categoria(1, "Eletrônicos")
    desktop1 = Desktop("Desktop Dell", "Preto", 3500, categoria1, "600W")
    notebook1 = Notebook("Notebook Lenovo", "Branco", 4000, categoria1, "10 horas")

    print("Informações do Desktop:")
    print(desktop1.getInformacoes())

    print("\nInformações do Notebook:")
    print(notebook1.getInformacoes())