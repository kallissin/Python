class Pessoa:
    ano_atual = 2020

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)


#p1 = Pessoa.por_ano_nascimento('Luis', 1987)
p1 = Pessoa('Luis', 32)
print(p1)
print(p1.nome, p1.idade)
p1.get_nascimento()