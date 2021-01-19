"""
Encapsulamento serve para esconder certas partes do codigo, para proteger a classe,
metodo ou atributo.

public, protected, private
"""


class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados

    def inserir_clientes(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_clientes(1, 'Otávio')
bd.inserir_clientes(2, 'Miranda')
bd.inserir_clientes(3, 'Rose')
bd.apaga_cliente(2)
bd.lista_clientes()
print(bd.dados)
print(bd._BaseDeDados__dados)
