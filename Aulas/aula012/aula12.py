"""
nome = 'Kelvin alisson cantarino'

if 'ss' in nome:
    print('Sim')
else:
    print('Não')
"""
usuario = input('Nome de usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'luis'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema')
else:
    print('Usuário ou senha invalida')