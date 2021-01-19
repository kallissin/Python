from abc import ABC

class Pessoa(ABC):
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade


class Cliente(Pessoa):
    def __init__(self, nome, idade, agencia, conta):
        super().__init__(nome, idade)

        self._agencia = agencia
        self._conta = conta

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta


