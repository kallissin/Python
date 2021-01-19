"""
combinations, permutations e product - itertools
combinação - ordem nao importa
permutação - ordem importa
ambos não repetem valores unicos
produto - Ordem importa e repete valores unicos.
"""
from itertools import combinations, permutations, product

pessoas = ['Maria', 'José', 'Camila', 'Kelvin', 'Bartira','Karine']
cont = 0
for grupo in product(pessoas, repeat=2):
    print(grupo)
    cont += 1
print(cont)