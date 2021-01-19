"""
Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - quantidade de casas decimais (float)
:(CARACTERE) (> ou < ou ^ ) (QUANTIDADE) (TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""
#num1 = 10
#num2 = 3
#divisao = num1 / num2
#nome = 'Kelvin'
#print(f'{nome:s}')
#print(f'{divisao:.2f}')
"""
num_1 = 1
print(f'{num_1:0>10}')

num_2 = 1150
print(f'{num_2:0>10.2f}')
"""
"""
nome = 'Kelvin'
sobrenome = 'alisson'
nome_formatado = '{1:#^50}'.format(nome, sobrenome)
print(nome_formatado)
"""

nome = 'Kelvin Alisson Cantarino'
print(nome.title())  # Primeira letra Maiusculo
print(nome.upper())  # Todas as letras Maiusculo
print(nome.lower())  # Todas as letras Minusculo










