'''
Iniciar com letra, pode conter números, separar _, letras minúsculas
'''

nome = 'kelvin'
idade = 25
altura = 1.80
e_maior = idade >= 18
data_1 = True
data_atual = 2020
peso = 80
imc = peso / (altura * altura)

"""
print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior de idade?:', e_maior)
"""

print(f'{nome} tem {idade} anos de idade e seu imc é {imc}')