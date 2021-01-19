"""
Operador Ternário
"""

"""
logger_user = False

if logger_user:
    msg = 'Usuário logado.'
else:
    msg = 'Usuário precisa logar'

print(msg)
"""
"""
logger_user = False
msg = 'Usuário logado' if logger_user else 'Usuário precisa logar'

print(msg)
"""
"""
idade = 18

if idade >= 18:
    print('pode acessar')
else:
    print('não pode acessar')
"""
idade = input('Qual a sua idade? ')

if not idade.isnumeric():
    print('Voce precisa digitar apenas numeros: ')
else:
    idade = int(idade)
    maior_idade = idade >= 18
    msg = 'Pode acessar' if maior_idade else 'Não pode acessar'
    print(msg)




