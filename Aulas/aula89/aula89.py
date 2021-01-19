"""
https://rszalski.github.io/magicmethods/
"""



class A:

    """

    def __new__(cls, *args, **kwargs):  #construtor
        if not hasattr(cls, '_jaexiste'):
            cls._jaexiste = object.__new__(cls)

        return cls._jaexiste
    """

    def __init__(self):
        pass
    """
    def __call__(self, *args, **kwargs):  #para executar os objetos como funcao
        resultado = 1

        for i in args:
            resultado *= i

        return resultado

    """
    def __setattr__(self, key, value):  #estou setando a chave e o valor
        self.__dict__[key] = value




a = A()
a.nome = 'Kelvin Alisson'
print(a.nome)
