class Cliente:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
        self.__enderecos = []

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @property
    def enderecos(self):
        return self.__enderecos


    def inseri_endereco(self, cidade, estado):
        self.__enderecos.append(Endereco(cidade, estado))

    def lista_enderecos(self):
        for endereco in self.__enderecos:
            print(endereco.cidade, endereco.estado)

    def __del__(self):
        print(f'{self.nome} FOI APAGADO')

class Endereco:
    def __init__(self, cidade, estado):
        self.__cidade = cidade
        self.__estado = estado

    @property
    def cidade(self):
        return self.__cidade

    @property
    def estado(self):
        return self.__estado

    def __del__(self):
        print(f'{self.estado}/{self.cidade} FOI APAGADO')




