"""
Desempacotamento de listas em python
"""

lista = ['Kelvin', 'Bartira', 'Maria', 1, 3, 4, 6, 8, 0, 9]

n1, n2, *outra_lista = lista
#n1 e n2 armazena os dois primeiros valores, o * serve para armazenar
# o restante da lista.
print(n1)
print(n2)