from aula94_resolucao.banco import Banco
from aula94_resolucao.cliente import Cliente
from aula94_resolucao.conta import ContaCorrente, ContaPoupanca

banco = Banco()

cliente1 = Cliente('Luis', 30)
cliente2 = Cliente('Maria', 45)
cliente3 = Cliente('Kelvin', 20)

conta1 = ContaPoupanca(1111, 123456, 0)
conta2 = ContaCorrente(2222, 654321, 0)
conta3 = ContaPoupanca(1234, 123654, 0)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

banco.inserir_conta(conta1)
banco.inserir_clientes(cliente1)
banco.inserir_conta(conta2)
banco.inserir_clientes(cliente2)
banco.inserir_conta(conta3)
banco.inserir_clientes(cliente3)

if banco.autenticar(cliente3):
    cliente1.conta.depositar(40)
    cliente1.conta.sacar(20)
else:
    print('Cliente não autenticado.')