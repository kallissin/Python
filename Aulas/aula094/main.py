from aula94.cc import ContaCorrente
from aula94.cp import ContaPoupanca
from aula94.banco import Banco


banco = Banco()

cliente1 = ContaCorrente('Kelvin Alisson Cantarino', 25, 333, 1111, 100)
banco.inserir_cliente(cliente1)
cliente1.depositar(300)
cliente1.sacar(500)


cliente2 = ContaPoupanca('Maria Helena Gomes de Sousa', 45, 333, 2222, 100)
banco.inserir_cliente(cliente2)
cliente2.depositar(500)
cliente2.sacar(150)

cliente3 = ContaCorrente('João pelé', 34, 333, 3333, 50)
banco.inserir_cliente(cliente3)
cliente3.depositar(150)
cliente3.depositar(100)
cliente3.sacar(200)


banco.lista_cliente()
banco.lista_conta()
