class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    @property
    def nome(self):  #Utilizamos o mesmo nome da variavel
        return self._nome  #Retornamos outro nome para não dar problema de loop

    @nome.setter
    #Aqui realizamos a alteração que precisamos
    def nome(self, valor):
        self._nome = valor.title()

    # Getter
    @property
    def preco(self):
        return self._preco

    # Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor


p1 = Produto('CAMISA', 50)
p1.desconto(10)
print(p1.nome, p1.preco)  #Agora irá passar nos construtores para configurar.

p2 = Produto('CANECA', 'R$15')
p2.desconto(10)
print(p2.nome, p2.preco)
