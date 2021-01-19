def saudacao(msg='Hello', nome='Maria'):
    msg = msg.replace('e', '3')
    nome = nome.replace('e', '3')
    return f'{msg}, {nome}'

variavel = saudacao()

print(variavel)
