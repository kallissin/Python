class Banco():
    def __init__(self):
        self._banco_dados = []
        self._agencia = 333
        self._clientes = []
        self._contas = []

    @property
    def banco_dados(self):
        return self._banco_dados

    @property
    def agencia(self):
        return self._agencia

    @property
    def clientes(self):
        return self._clientes

    @property
    def contas(self):
        return self._contas

    def inserir_cliente(self, cliente):
        self._banco_dados.append(cliente)

    def lista_cliente(self):
        for cliente in self._banco_dados:
            self._clientes.append(cliente._nome)
        print(self._clientes)


    def lista_conta(self):
        for contas_bancarias in self._banco_dados:
            self._contas.append(contas_bancarias._conta)
        print(self._contas)
