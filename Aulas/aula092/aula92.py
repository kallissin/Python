"""


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)

        if 'b_fala' not in namespace:
            print(f'Oi, Você precisa criar o método b_fala em {name}')
        else:
            if not callable(namespace['b_fala']):
                print(f'b_fala precisa ser um método, não atributo em {name}.')
        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    def fala(self):
        self.b_fala()


class B(A):

    def b_fala(self):
        print('oi')
"""
"""
class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)
        if 'attr_classe' in namespace:
            pass
        del namespace['attr_classe']
        return type.__new__(mcs, name, bases, namespace)

class A(metaclass=Meta):
    attr_classe = 'valor A'

class B(A):
    attr_classe = 'valor B'

b = B()
print(b.attr_classe)

"""

class Pai:
    nome = 'Teste'

A = type('A',(),{'attr': 'Olá Mundo'})

a = A()
print(a.attr)