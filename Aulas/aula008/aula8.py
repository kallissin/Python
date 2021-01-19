"""
* Criar variáveis para nome (str), idade (int),
* altura (float) e peso (float) de ua pessoa
* Criar variáveis com o ano atual (int)
* obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir un texto com todos os valores na ela usando F-Strings (com as chaves)
"""

nome = 'Kelvin Cantarino'
idade = 25
altura = 1.80
peso = 85
ano_atual = 2020
data_nasc = ano_atual - idade
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.')
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {data_nasc}.')
