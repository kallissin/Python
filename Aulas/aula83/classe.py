class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__
    def falar(self):
        print(f'{self.nomeclasse} falando...')

class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} comprando...')

    def falar(self):
        print('Cliente falando')

class ClienteVip(Cliente):
    def __init__(self, nome, idade, sobrenome):
        Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome


    def falar(self):
        #super().falar()  # se rerefe a classe super classe. no caso "Cliente"
        Pessoa.falar(self)  #se refere a classe pessoa e ao metodo falar.
        #print('Olá mundo')
        print(f'{self.nome} {self.sobrenome}')