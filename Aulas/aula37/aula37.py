"""
Funções (def) em Python - *args **kwargs -
"""
"""
def func(n1, n2, n3, n4, n5, nome=None, n6=None):
    return n1, n2, n3, n4, n5, nome, n6

var = func(1, 2, 3, 4, 5, nome='kelvin', n6=6)
print(type(var))
"""

def func(*args, **kwargs):
    print(args)
    print(args[0])
    nome = kwargs.get('nome')
    print(nome)
    idade = kwargs.get('idade')

    if idade is not None:
        print(idade)
    else:
        print('Idade não existe')

lista = ['Amor', 'Maria', 'João']
func(*lista, 1, 2, 3, 4, nome='Kelvin', sobrenome='Alisson', idade=19)
