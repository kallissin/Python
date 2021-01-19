from random import randint


class Pessoa:
    ano_atual = 2020

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nscimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand


# p1 = Pessoa('Kelvin', 25)
p1 = Pessoa.por_ano_nascimento('Kelvin', 1995)
print(p1.idade)
print(Pessoa.gera_id())
print(p1.gera_id())
