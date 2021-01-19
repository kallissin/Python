variavel = 'valor'

def func(arg=variavel):
    arg = arg.replace('v', 'c')
    return arg

nova_variavel = func(arg=variavel)
print(variavel)
print(nova_variavel)
