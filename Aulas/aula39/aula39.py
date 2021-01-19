"""
1 - Crie uma função1 que recebe uma função2 como parâmetro e
retorne o valor da função2 executada.

def mestre():
    return f'Olá, mundo'

def iniciar(mestre):
    return mestre()

var = iniciar(mestre)
print(var)

"""
"""
2 - Crie uma função1 que recebe uma função2 como parâmetro e 
retorne o valor da função2 executada. Faça a função1 executar 
duas funções que receba um número diferente de argumentos
"""
def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def identidade(nome):
    return f'Olá {nome}'

def saudacao(nome, saudacao):
    return f'{nome}, {saudacao}'

var = mestre(identidade, 'kelvin')
var2 = mestre(saudacao, 'Joaozinho', saudacao='Bom dia')
print(var)
print(var2)