from aula94.conta import Conta
from aula94.banco import Banco

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insulficiente')
            return
        self.saldo -= valor
        self.extrato()
