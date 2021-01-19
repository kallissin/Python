from abc import abstractmethod
from aula94.cliente import Cliente


class Conta(Cliente):
    def __init__(self, nome, idade, agencia, conta, saldo):
        super().__init__(nome, idade, agencia, conta)

        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Saldo precisa ser numérico')
        self._saldo = valor

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('valor do depósito precisa ser numérico')
        self._saldo += valor
        self.extrato()

    def extrato(self):
        print(f'Agencia: {self._agencia}', end=' ')
        print(f'Conta: {self._conta}', end=' ')
        print(f'Saldo: {self._saldo}')

    @abstractmethod
    def sacar(self, valor):
        pass
