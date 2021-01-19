class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.classe_nome = self.__class__.__name__

    def falar(self):
        print(f'{self.classe_nome} falando.....')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.classe_nome} esta comprando...')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.classe_nome} esta estudando...')
